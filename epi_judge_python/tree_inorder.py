from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    in_order = []
    traversal_stack = [tree]
    while traversal_stack:
        node = traversal_stack.pop()
        if node.right:
            traversal_stack.append(node.right)
        if node.left:
            traversal_stack.append(node.left)

    return answ[::-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))