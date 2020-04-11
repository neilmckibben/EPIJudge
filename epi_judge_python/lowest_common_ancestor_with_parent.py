import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def node_height(node):
    height = 0
    while node.parent:
        node = node.parent
        height += 1
    return height
    
def lca(node0: BinaryTreeNode,
    node_0_height = node_height(node0)
    node_1_height = node_height(node1)
    deepest, shortest, deepest_height, shortest_height = node0, node1, node_0_height, node_1_height
    if node_1_height > node_0_height:
        deepest, shortest, deepest_height, shortest_height = node1, node0, node_1_height, node_0_height

    while deepest_height != shortest_height:
        deepest = deepest.parent
        deepest_height -= 1

    while deepest is not shortest:
        deepest, shortest = deepest.parent, shortest.parent
    return deepest


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
