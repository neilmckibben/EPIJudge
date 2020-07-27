from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    pivot =  find_pivot(A)
    return pivot

def find_pivot(A):
    if len(A) <= 2:
        if len(A) == 2 and A[0] > A[1]:
            return 1
        else:
            return 0
    #Binary search for pivot
    L, U = 0, len(A) - 1
    while L <= U:
        mid = L + (U - L) // 2
        mid_val, low_val, high_val = A[mid], A[L], A[U]
        if A[mid] < A[mid - 1]: #Found the pivot
            return mid
        elif A[mid] > A[U]:
            L = mid + 1
        else:
            U = mid - 1
    return 0

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
