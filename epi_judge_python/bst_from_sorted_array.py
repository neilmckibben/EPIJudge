import functools
from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import (binary_tree_height,
                                              generate_inorder)
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def build_min_height_bst_from_sorted_array(A: List[int]) -> Optional[BstNode]:
    root = None
    if len(A) != 0:
        middle = len(A) // 2
        root = BstNode(A[middle])
        left_arr = A[:middle]
        right_arr = A[middle + 1:]
        root.left = build_min_height_bst_from_sorted_array(left_arr)
        root.right = build_min_height_bst_from_sorted_array(right_arr)
    return root


@enable_executor_hook
def build_min_height_bst_from_sorted_array_wrapper(executor, A):
    result = executor.run(
        functools.partial(build_min_height_bst_from_sorted_array, A))

    if generate_inorder(result) != A:
        raise TestFailure('Result binary tree mismatches input array')
    return binary_tree_height(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'bst_from_sorted_array.py', 'bst_from_sorted_array.tsv',
            build_min_height_bst_from_sorted_array_wrapper))
