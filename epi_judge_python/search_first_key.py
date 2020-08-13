from typing import List

from test_framework import generic_test
import bisect


def search_first_of_k(A: List[int], k: int) -> int:
    l,r, = 0, len(A) - 1
    canidate = -1
    while l <= r:
        mid = l + (r - l) // 2
        if A[mid] == k:
            canidate = mid
            r = canidate - 1
        elif A[mid] < k:
            l = mid + 1
        else:
            r = mid - 1
    return canidate



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
