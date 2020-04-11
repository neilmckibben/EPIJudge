from test_framework import generic_test


def rabin_karp(t: str, s: str) -> int:
    if len(s) is 0:
        return 0
    for i in range(0, len(t)):
        if t[i] == s[0]:
            j = 1
            valid = True
            while j < len(s) and valid and i + j < len(t):
                valid = (t[i + j] == s[j])
                j += 1
            if valid and j == len(s):
                return i
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
