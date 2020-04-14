from typing import List

from test_framework import generic_test



def can_reach_end(A: List[int]) -> bool:
    start = 0
    if (len(A) - 1) == start:
        return True
    j = 0
    element = 0
    while j < element + 1:
        next_val = A[j]
        element = max(element, j + next_val)
        if j == len(A) - 1:
            return True
        j += 1
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
