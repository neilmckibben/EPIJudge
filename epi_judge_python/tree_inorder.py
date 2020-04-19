from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    if not tree:
        return []
    in_order = []
    first = (tree, True)
    if tree and not tree.left:
        first = [tree, False]
    traversal_stack = [first]
    while traversal_stack:
        element = traversal_stack.pop()
        node, has_left = element[0], element[1]
        data = (node.data)
        if has_left:
            traversal_stack.append([node, False])
            traversal_stack.append([node.left, node.left.left is not None])
        else:
            in_order.append(node.data)
            if node.right:
                traversal_stack.append([node.right, node.right.left is not None])

    return in_order


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))