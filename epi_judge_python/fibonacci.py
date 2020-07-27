from test_framework import generic_test


def fibonacci(n: int) -> int:
    a, b, c, = 1, 1, 0
    if n == 0:
        return 0
    if n <= 2:
        return 1
    i = 2
    while i < n:
        c = a + b
        a, b = b, c
        i += 1
    return b


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
