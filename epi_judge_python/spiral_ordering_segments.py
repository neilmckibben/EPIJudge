from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
    # TODO - you fill in here.
    if len(square_matrix) is 0:
        return []
    if len(square_matrix) is 1:
        return [1]
    # spiral = [[-1] * len(square_matrix[0]) for i in range(len(square_matrix))]
    spiral = [[-1 for i in range(len(square_matrix[0]))] for j in range(len(square_matrix))]
    size = len(square_matrix) * len(square_matrix[0])
    i, j, counter = 0, 0, 0
    value = 1
    while value <= size:
        # Move to the right in the array
        for k in range(i, len(square_matrix[0]) - i):
            if spiral[j][k] is not -1:
                break
            spiral[j][k] = value
            value += 1
        # Reach the end, so we begin filling downwards
        for k in range(j + 1, len(square_matrix) - j):
            if spiral[k][(len(square_matrix[0]) - 1 - i)] is not -1:
                break
            spiral[k][(len(square_matrix[0]) - 1 - i)] = value
            value += 1
        # Begin filling to the left
        for k in range(i + 1, len(square_matrix[0])):
            if spiral[len(square_matrix) - 1 - j][k] is not -1:
                break
            spiral[len(square_matrix) - 1 - j][k] = value
            value += 1
        # Begin filling up
        for k in range(j, len(square_matrix)):
            a = spiral[i][len(square_matrix) - 1 - k]
            if spiral[i][len(square_matrix) - 1 - k] is not -1:
                break
            spiral[i][len(square_matrix) - 1 - k] = value
            value += 1
        j += 1
        i += 1

    return spiral


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
