from typing import List

from test_framework import generic_test


def minimum_path_weight(triangle: List[List[int]]) -> int:
    if not triangle:
        return 0
    for i in range(1, len(triangle)):
        row = triangle[~i]
        prev_row = triangle[~i + 1]
        for j, element in enumerate(row):
            min_one, min_two = prev_row[j], prev_row[j + 1]
            triangle[~i][j] += min(min_one, min_two)
    return triangle[0][0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'minimum_weight_path_in_a_triangle.py',
            'minimum_weight_path_in_a_triangle.tsv', minimum_path_weight))
