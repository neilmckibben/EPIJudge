import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def find_node_in_subtree(tree, node):
    if tree is not None:
        if tree is node:
            return True
        return find_node_in_subtree(tree.left, node) or find_node_in_subtree(tree.right, node)
    return False

def both_nodes_in_subtree(tree, node0, node1):
    in_tree = find_node_in_subtree(tree, node0) and find_node_in_subtree(tree, node1)
    if in_tree:
        in_left = find_node_in_subtree(tree.left, node0) and find_node_in_subtree(tree.left, node1)
        in_right = find_node_in_subtree(tree.right, node0) and find_node_in_subtree(tree.right, node1)
        if in_left:
            return both_nodes_in_subtree(tree.left, node0, node1)
        if in_right:
            return both_nodes_in_subtree(tree.right, node0, node1)
        return tree

def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    return both_nodes_in_subtree(tree, node0, node1)



@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
