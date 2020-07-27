import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))

def compare_start(start, new_start):
    #Return the minimum start value
    if start.val < new_start.val:
        return start
    elif start.val > new_start.val:
        return new_start
    elif start.is_closed:
        return start
    else:
        return new_start



def compare_end(end, new_end):
    if end.val > new_end.val:
        return end
    elif end.val < new_end.val:
        return new_end
    elif end.is_closed:
        return end
    else:
        return new_end


def union_of_intervals(intervals: List[Interval]) -> List[Interval]:
    ans = []
    intervals.sort(key=lambda x: (x.left.val, not x.left.is_closed))
    if intervals:
        ans = [intervals[0]]
        for i, interval in enumerate(intervals[1:]):
            #Check if interval is in previous interval without regard for open and close crap
            new_start, new_end = interval.left, interval.right
            start, end = ans[-1].left, ans[-1].right
            if new_start.val < end.val:
                #Merge intervals
                ans[-1] = Interval(compare_start(start, new_start), compare_end(end, new_end))
            elif new_start.val == end.val and (new_start.is_closed or end.is_closed):
                ans[-1] = Interval(compare_start(start, new_start), compare_end(end, new_end))
            else:
                ans.append(interval)
    return ans


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intervals_union.py',
                                       'intervals_union.tsv',
                                       union_of_intervals_wrapper))


#Error at (176, False, 183, False), (183, True, 192, True) -> (176, False, 192, True)