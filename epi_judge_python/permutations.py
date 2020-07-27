from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    ans = []
    permute([], A, ans)

    return ans


def permute(path, values, ans):
    if len(values) == 0:
        if path not in ans:
            ans.append(path)
        return
    for i, val in enumerate(values):
        front, back = values[i-1:], values[:i + 1]
        permute(path + [val], values[:i] + values[i + 1:], ans)
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
