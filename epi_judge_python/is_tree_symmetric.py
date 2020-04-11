from test_framework import generic_test

def parse(left, right):
    if left is None and right is None:
        return True
    elif left is None or right is None:
        return False
    elif left.data != right.data:
        return False

    return parse(left.left, right.right) and parse(left.right, right.left)

def is_symmetric(tree):
    if tree:
        return parse(tree.left, tree.right)
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
