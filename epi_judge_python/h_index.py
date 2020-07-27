from typing import List

from test_framework import generic_test


def h_index(citations: List[int]) -> int:
    citations.sort()
    ans = 0
    for i in range(0, len(citations)):
        if citations[~i] >= ans + 1:
            ans += 1
    return ans


if __name__ == '__main__':
    exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))
