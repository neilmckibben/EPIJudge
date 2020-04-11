import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def leaves(node, exterior_path):
    if node:
        leaves(node.left, exterior_path)
        leaves(node.right, exterior_path)
        if not node.left and not node.right:
            exterior_path.append(node)

def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    copy = tree
    exterior_path = list()
    while copy:
        if copy.left or copy.right:
            exterior_path.append(copy)
        if copy.left:
            copy = copy.left
        else:
            copy = copy.right
    leaves(tree, exterior_path)
    copy = tree.right
    sub_list = list()
    while copy:
        if copy.left or copy.right:
            sub_list.append(copy)
        if copy.right:
            copy = copy.right
        else:
            copy = copy.left
    exterior_path.extend(sub_list[::-1])
    return exterior_path


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_exterior.py', 'tree_exterior.tsv',
                                       create_output_list_wrapper))
