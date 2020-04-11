from test_framework import generic_test

def is_balanced_binary_tree(tree):
    copy = tree
    max_depth = 0
    while copy:
        tree = tree.left
        max_depth += 1
    copy = tree
    right_depth = 0
    while copy:
        tree = tree.right
        right_depth += 1

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
