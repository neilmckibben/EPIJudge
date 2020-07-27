from typing import List

from test_framework import generic_test


def smallest_nonconstructible_value(A: List[int]) -> int:
    A.sort()
    # print("\n", A)
    if A:
        if A[0] != 1:
            return 1
    max_certain = 0
    prev = 0
    for num in A:
        if prev < num - 1:
            return prev + 1
        prev += num
        max_certain += num
    return max_certain + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('smallest_nonconstructible_value.py',
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
