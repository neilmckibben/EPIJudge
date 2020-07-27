from typing import Optional

from bst_node import BstNode
from test_framework import generic_test
import bisect


def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    path = process(tree, [])
    index = path.index(k)
    if index:
        if index != len(path) - 1:
            return path[index + 1]
        else:
            return path[index - 1]
    return None


def process(tree: BstNode, path: list) -> list:
    if tree:
        process(tree.left, path)
        path.append(tree)
        process(tree.right, path)
    return path



def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
