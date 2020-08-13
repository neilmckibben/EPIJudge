from test_framework import generic_test


def square_root(x: float) -> float:
    l, r = 0, x

    while l <= r:
        mid = l + (r - l) // 2
        value = mid ** 2
        if value == x:
            return mid
        elif value < x:
            l = mid
        else:
            r = mid
    return 0.0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('real_square_root.py',
                                       'real_square_root.tsv', square_root))
