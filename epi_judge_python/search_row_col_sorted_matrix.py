from typing import List

from test_framework import generic_test


def matrix_search(A: List[List[int]], x: int) -> bool:
    #Start at top right
    if len(A) > 0:
        row, column = 0, 0
        while row < len(A) and column < len(A[0]):
            top_right = A[row][~column]
            if top_right == x:
                return True
            if top_right > x:
                column += 1
            else:
                row += 1
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_row_col_sorted_matrix.py',
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))





[1, 5]
[2, 6]