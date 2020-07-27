from test_framework import generic_test


def square_root(k: int) -> int:
    if k == 0:
        return 0
    elif k <= 3:
        return 1
    elif k <= 8:
        return 2
    L, U = 0, k // 3
    while L <= U:
        mid = L + (U - L) // 2
        if mid * mid <= k < (mid + 1) ** 2:
            return mid
        elif mid * mid < k:
            L = mid + 1
        else:
            U = mid - 1
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
