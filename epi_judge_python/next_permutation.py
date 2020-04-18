from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    perm_sort = sorted(perm)

    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
