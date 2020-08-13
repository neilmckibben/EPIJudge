from typing import List

from test_framework import generic_test


def minimum_total_waiting_time(service_times: List[int]) -> int:
    service_times.sort()
    prev = 0
    waiting_time = 0
    for time in service_times:
        waiting_time += prev
        prev += time

    return waiting_time


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_waiting_time.py',
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))