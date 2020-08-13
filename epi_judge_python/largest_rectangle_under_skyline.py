from typing import List

from test_framework import generic_test


def calculate_largest_rectangle(heights: List[int]) -> int:

    front, back = 0, len(heights) - 1
    maxArea = 0
    while front < back:
        min_height_in_range = min(heights[front:back + 1])
        area = min_height_in_range * (back - front + 1)
        maxArea = max(area, maxArea)
        if heights[front] <= heights[back]:
            front += 1
        else:
            back -= 1


    return maxArea


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('largest_rectangle_under_skyline.py',
                                       'largest_rectangle_under_skyline.tsv',
                                       calculate_largest_rectangle))
