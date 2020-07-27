from test_framework import generic_test


def number_of_ways(n: int, m: int) -> int:
    matrix = [[0] * n for _ in range(m)]
    if len(matrix) > 0:
        for i in range(0, len(matrix[0])):
            matrix[0][i] = 1
        for i in range(0, len(matrix)):
            matrix[i][0] = 1
    def calculate(row, column):
        if row > 0 and row < len(matrix[0]) and column > 0 and column < len(matrix):
            matrix[column][row] = matrix[column - 1][row] + matrix[column][row - 1]
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            calculate(j, i)
    return matrix[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
