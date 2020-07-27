import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    # Sort by start time
    max_events = 0
    encoding = [0]
    if A:
        A.sort()
        # Get time range
        max_time = 0
        for event in A:
            max_time = max(max_time, event[1])
        max_time += 1
        encoding = list([0] * max_time)
        for event in A:
            start, end = event
            for i in range(start, end + 1):
                encoding[i] += 1
    return max(encoding)


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))

