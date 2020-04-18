import heapq
from typing import List
from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    ##Review, this is not the optimal implementation.
    min_heap = []
    element = 0
    for line in sorted_arrays:
        for value in line:
            heapq.heappush(min_heap, value)
            element += 1
    return heapq.nsmallest(element, min_heap)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
