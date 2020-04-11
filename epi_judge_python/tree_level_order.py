from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if tree is None:
        return []
    order = list()
    level = deque()
    level.append([tree])
    while len(level) != 0:
        sub_level = level.popleft()
        next_sub_level = deque()
        values = []
        for node in sub_level:
            values.append(node.data)
            if node.left is not None:
                next_sub_level.append(node.left)
            if node.right is not None:
                next_sub_level.append(node.right)
        if len(sub_level) != 0:
            level.append(next_sub_level)
            order.append(values)
    return order

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
