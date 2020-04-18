from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    if len(square_matrix) is 0:
        return []
    spiral = []
    not_done = True
    i, j = 0, len(square_matrix[0]) - 1
    front, back = len(square_matrix[0]), len(square_matrix)
    while not_done:
        for k in range(0, front):
            spiral.append(square_matrix[i][k])
        i += 1
        for k in range(i, back):
            spiral.append(square_matrix[j][k])
        j -= 1
        for k in range(0, j):
            spiral.append(square_matrix[~k][j])
        for k in range()
        not_done = False
    print(spiral)

    return spiral


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
