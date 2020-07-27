from typing import List

from test_framework import generic_test


def minimum_path_weight(triangle: List[List[int]]) -> int:
    minimum_path = 0
    for row in triangle:
        minimum_path += min(row)
    return minimum_path


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'minimum_weight_path_in_a_triangle.py',
            'minimum_weight_path_in_a_triangle.tsv', minimum_path_weight))
