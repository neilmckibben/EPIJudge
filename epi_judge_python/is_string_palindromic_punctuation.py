from test_framework import generic_test


def is_palindrome(s):
    invalid = {" ", ",", ".", "!", "%", "^", "?", "[", "]", "(", ")", "+", "&", "%", "$", "#", ":", ";", "%", "_", "-",
               "{", "}", "\\", "/", "'", ">", "<", "\"", "="}
    s = [i for i in s if i not in invalid]
    i = 0
    for i in range(0, len(s)//2):
        if s[i].lower() != s[-1 - i].lower():
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_palindromic_punctuation.py",
                                       "is_string_palindromic_punctuation.tsv",
                                       is_palindrome))
