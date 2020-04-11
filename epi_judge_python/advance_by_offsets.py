from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
        value = False
        if (len(A) - 1) == start:
            return True
        for i in range(start + 1, length + start + 1):
            if evaluate(A, i, A[i]):
                return True
        return value
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
