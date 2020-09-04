from typing import List

from test_framework import generic_test


def fill_surrounded_regions(board: List[List[str]]) -> None:
    for a in board:
        print(a)
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == "W":
                #Check if 3 or more of the surrounding regions are white
                if 0 < i  < len(board) - 1 and 0 < j < len(board[0]) - 1:
                    top, bottom, left, right = board[i][j + 1], board[i][j - 1], board[i - 1][j], board[i + 1][j]
                    multiple = [top, bottom, left, right]
                    if multiple.count("B") >= 3:
                        board[i][j] = "-"
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == "-":
                board[i][j] = "B"
    print("----------------")
    for a in board:
        print(a)
    return


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
