from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    mapping = dict()
    closest_words = float('inf')
    for i, word in enumerate(paragraph):
        if word in mapping:
            closest_words = min(i - mapping[word], closest_words)
        mapping[word] = i
    if closest_words == float('inf'):
        closest_words = -1
    return closest_words


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
