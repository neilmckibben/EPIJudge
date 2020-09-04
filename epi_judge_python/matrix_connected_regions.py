from typing import List

from test_framework import generic_test


def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    desired_color = not image[x][y]
    checked_positions = set()
    def fill(a, b):
        if 0 <= a < len(image) and 0 <= b < len(image[0]) and image[a][b] != desired_color and (
                a, b) not in checked_positions:
            image[a][b] = desired_color
            fill(a - 1, b)
            fill(a + 1, b)
            fill(a, b - 1)
            fill(a, b + 1)
            checked_positions.add((a, b))
    fill(x, y)
    return


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
