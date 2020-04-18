from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    left = parse(tree.left)
    right = parse(tree.right)
    return True

def parse(tree):
    if tree:
        height = 1
        height_left = parse(tree.left)
        height_right = parse(tree.right)
        if height_left or height_right
    return 0
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
