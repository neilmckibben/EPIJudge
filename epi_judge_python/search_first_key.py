from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    pivot = find_pivot(A)
    #Binary search w/ pivot information
    front, back = A[0], A[-1]
    L, U = 0, len(A) - 1
    if front <= k <= A[pivot - 1]: #Values is in the left subarray
        U = pivot - 1
        if pivot - 1 == -1:
            U = len(A) - 1
    else:
        L = pivot
    while L <= U:
        mid = L + (U - L) // 2
        if A[mid] == k: #Found the pivot
            return mid
        elif A[mid] < k:
            L = mid + 1
        else:
            U = mid - 1
    return -1

def find_pivot(A):
    if len(A) <= 2:
        if A[0] > A[1]:
            return 1
        else:
            return 0
    #Binary search for pivot
    L, U = 0, len(A) - 1
    while L <= U:
        mid = L + (U - L) // 2
        if A[mid] < A[mid - 1]: #Found the pivot
            return mid
        elif A[mid] < A[L]:
            L = mid
        else:
            U = mid - 1
    return -1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))


[4, 5, 6, 7, 0, 1, 2, 3]
