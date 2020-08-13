import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))


def find_minimum_visits(intervals: List[Interval]) -> int:
    #Assume sorted
    intervals.sort()
    print(merge_intervals(intervals))
    return 2

def merge_intervals(intervals):
    merged = []
    if len(intervals) != 0:
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            canidate = merged[-1]
            interval = intervals[i]
            if canidate.left <= interval.left <= canidate.right:
                merged[-1] = Interval(canidate.left, min(interval.right, canidate.right))
            elif canidate.left <= interval.right <= canidate.right:
                merged[-1] = Interval(max(canidate.left, interval.left), min(canidate.right, interval.right))



    return merged

@enable_executor_hook
def find_minimum_visits_wrapper(executor, A):
    A = [Interval(*a) for a in A]
    return executor.run(functools.partial(find_minimum_visits, A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'minimum_points_covering_intervals.py',
            'minimum_points_covering_intervals.tsv',
            find_minimum_visits_wrapper))
