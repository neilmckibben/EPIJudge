import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    matrix = [[-1] * (capacity + 1) for _ in items]

    def calculate(item, capacity):
        if item < 0:
            return 0
        if matrix[item][capacity] == -1:
            clock = items[item]
            if clock.weight > capacity:
                matrix[item][capacity] = 0
            else:
                without_clock = calculate(item - 1, capacity - clock.weight)
                with_clock = clock.value + calculate(item, capacity - clock.weight)
                matrix[item][capacity] = max(with_clock, without_clock)

        return matrix[item][capacity]

    return calculate(len(items) - 1, capacity)


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
