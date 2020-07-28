from typing import List

from test_framework import generic_test


def minimum_messiness(words: List[str], line_length: int) -> int:
    matrix = [[0] * len(words) for _ in words]

    def calculate(word_index):
        if words and matrix[word_index][word_index] == 0:
            error =
        
        return matrix[word_index][word_index]

    calculate(len(words) - 1)
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pretty_printing.py',
                                       'pretty_printing.tsv',
                                       minimum_messiness))
