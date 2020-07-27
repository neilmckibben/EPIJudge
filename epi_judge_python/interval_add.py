import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))


def add_interval(disjoint_intervals: List[Interval],
                 new_interval: Interval) -> List[Interval]:
    if disjoint_intervals:
        disjoint_intervals.sort()
        i = 0
        new_start, new_end = new_interval.left, new_interval.right
        if new_start < disjoint_intervals[0].right and new_end < disjoint_intervals[0].left: #Should just be appended to the front
            return [new_interval] + disjoint_intervals
        while i < len(disjoint_intervals):
            element = disjoint_intervals[i]
            start, end = element.left, element.right
            #Check if its within the interval
            # if new_start <= start <= new_end or new_start <= end <= new_end or start <= new_end <= end or start <= new_start <= end:
            if new_start <= end and new_end >= start:
                start, end = min(new_start, start), max(new_end, end)
                # print("Hit", start, end)
                #Merge intervals
                index_start = i
                i += 1
                while i < len(disjoint_intervals) and disjoint_intervals[i].left <= end:
                    end = max(end, disjoint_intervals[i].right)
                    i += 1
                disjoint_intervals[index_start] = Interval(start, end)
                del disjoint_intervals[index_start + 1 : i]
                return disjoint_intervals
            i += 1
    return sorted(disjoint_intervals + [new_interval])


@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
    disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
    return executor.run(
        functools.partial(add_interval, disjoint_intervals,
                          Interval(*new_interval)))


def res_printer(prop, value):
    def fmt(x):
        return [[e[0], e[1]] for e in x] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('interval_add.py',
                                       'interval_add.tsv',
                                       add_interval_wrapper,
                                       res_printer=res_printer))
# new_interval: [724, 727]
