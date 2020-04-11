from typing import List

from test_framework import generic_test

from test_framework import generic_test

def rotate_matrix(square_matrix: List[List[int]]) -> None:
    rotated = [[] for i in range(0, len(square_matrix))]
    if len(square_matrix) is 0:
        return []
    if len(square_matrix) is 1:
        return square_matrix
    for i in range(0, len(square_matrix)):
        row = square_matrix[len(square_matrix) - 1 - i] #Grab whole row
        for j in range(0, len(row)):
            rotated[j].append(row[j])
    return rotated

def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_rotation.py',
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
