from typing import List

from test_framework import generic_test


def matrix_search(A: List[List[int]], x: int) -> bool:
    #Sort columns
    back = A[-1][-1]
    i = 0
    while i < len(A):
        back = A[~i][-1]
        i += 1
    for value in A[~(i - 1)]:
        if value == x:
            return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_row_col_sorted_matrix.py',
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
