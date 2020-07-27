from typing import List

from test_framework import generic_test


def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:
    def dfs(row, column, patternIndex):
        if patternIndex >= len(pattern):
            return True
        if 0 <= row < len(grid) and 0 <= column < len(grid[0]) and grid[row][column] == pattern[patternIndex]:
            return dfs(row + 1, column, patternIndex + 1) or dfs(row - 1, column, patternIndex + 1) or \
                   dfs(row, column + 1, patternIndex + 1) or dfs(row, column - 1, patternIndex + 1)
        return False

    if not pattern:
        return True
    for rowIndex, row in enumerate(grid):
        for columnIndex, element in enumerate(row):
            if dfs(rowIndex, columnIndex, 0):
                return True

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
