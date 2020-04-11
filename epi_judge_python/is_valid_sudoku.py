from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    #Check row
    valid_rows = [[] for i in range(9)]
    valid_columns = [[] for i in range(9)]
    valid_square = [[] for i in range(9)]
    for i in range(0, len(partial_assignment)):
        for j in range(0, len(partial_assignment[0])):
            value = partial_assignment[i][j]
            if value:
                square = ((i//3) * 3) + j//3
                if value in valid_rows[j] or value in valid_columns[i] or value in valid_square[square]:
                    return False
                valid_rows[j].append(value)
                valid_columns[i].append(value)
                valid_square[square].append(value)
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
