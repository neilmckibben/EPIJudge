from typing import List
import collections
from test_framework import generic_test


def find_all_substrings(s: str, words: List[str]) -> List[int]:
    indexes = []
    if words:
        chunking_size, i = len(words[0]), 0
        while i < len(s):
            temp_list = collections.Counter(words)
            substring = s[i:i+chunking_size]
            j = i
            while substring in temp_list:
                temp_list[substring] -= 1
                if temp_list[substring] == 0:
                    del temp_list[substring]
                if len(temp_list) == 0:
                    indexes.append(i)
                j += chunking_size
                substring = s[j:j + chunking_size]
            i += 1
    return indexes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'string_decompositions_into_dictionary_words.py',
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
