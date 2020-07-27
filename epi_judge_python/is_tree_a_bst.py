from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    path = process(tree, [])
    prev = float('-inf')
    for i in range(0, len(path)):
        if path[i] < prev:
            print(path[i], prev)
            return False
        prev = path[i]
    return True


def process(tree: BinaryTreeNode, path: list) -> list:
    valid = True
    if tree:
        valid_left = process(tree.left, path)
        path.append(tree.data)
        valid_right = process(tree.right, path)
    return path

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
