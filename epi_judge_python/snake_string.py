from test_framework import generic_test


def snake_string(s: str) -> str:
    top, middle, bottom = [], [], []
    i = 0
    while i < len(s):
        middle.append(s[i])
        i += 2
    i = 1
    counter = 0
    while i < len(s):
        if counter % 2 == 0:
            top.append(s[i])
        else:
            bottom.append(s[i])
        counter += 1
        i += 2
    top.extend(middle)
    top.extend(bottom)
    snaked = "".join(top)
    return snaked


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('snake_string.py', 'snake_string.tsv',
                                       snake_string))
