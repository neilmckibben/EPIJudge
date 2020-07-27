from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    #Reverse inorder traversal (sorta)
    path = []
    stack = [tree]
    while k != 0 and stack:
        tree = stack.pop()
        if tree:
            if tree.left:
                stack.append(tree.left)
            if not tree.right:
                #Current node is the right most value
                path.append(tree.data)
                k -= 1
            else:
                #Keeping going right, but save the current node too
                right = tree.right
                tree.left, tree.right = None, None #Prune the tree
                stack.append(tree)
                stack.append(right)

    return path

def inorder_traversal(node, path):
    if node:
        inorder_traversal(node.left, path)
        path.append(node.val)
        inorder_traversal(node.right, path)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
