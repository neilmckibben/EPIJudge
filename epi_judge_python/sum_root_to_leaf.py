from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def parse(tree: BinaryTreeNode, values: list, path: str):
    if tree:
        path += str(tree.data)
        if tree.left or tree.right:
            if tree.left:
                parse(tree.left, values, path)
            if tree.right:
                parse(tree.right, values, path)
        else:
            values.append(path)



def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    values = list()
    parse(tree, values, "")
    sum = 0
    for value in values:
        sum += int(value, 2)
    return sum

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
