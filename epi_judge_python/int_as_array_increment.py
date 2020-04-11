from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    if A[-1] + 1 > 9:
        A[-1] = 0
        remainder = True
        for i in range(1, len(A)):
            if A[len(A) - 1 - i] + 1 > 9:
                A[len(A) - 1 - i] = 0
            else:
                A[len(A) - 1 - i] += 1
                remainder = False
                break
        if remainder:
            A.insert(0, 1)
    else:
        A[-1] += 1
    return A

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
