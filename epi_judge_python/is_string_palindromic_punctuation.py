from test_framework import generic_test


def is_palindrome(s):
    length = len(s)
    unchecked = True
    while(unchecked)
        front = i
        back = length - 1 - i
        frontChar = s[front]
        backChar = s[back]
        if s[front] is not s[back]:
            return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_palindromic_punctuation.py",
                                       "is_string_palindromic_punctuation.tsv",
                                       is_palindrome))
