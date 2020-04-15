from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:
    for i in range(0, len(perm)):
        while i != perm[i]:
            A[i], A[perm[i]] = A[perm[i]], A[i]
            perm[perm[i]], perm[i] = perm[i], perm[perm[i]]
    return


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
# [7, 2, 11, 10, 4, 1, 15, 3, 9, 17, 18, 16, 14, 5, 0, 8, 6, 12, 13]
# [3, 2, 11, 7, 4, 1, 15, 3, 9, 17, 18, 16, 14, 5, 0, 8, 6, 12, 13]