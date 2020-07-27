from typing import List

from test_framework import generic_test


def palindrome_decompositions(text: str) -> List[List[str]]:
    answer = []
    return generate([], text, answer)

def generate(path, text, answer):
    if len(text) == 0:
        answer.append(path)
    if text == str(text[::-1]):
        answer.append(path + [text])
    for i in range(0, len(text)):
        sub_str = text[:~i]
        if sub_str == sub_str[::-1]:
            generate(path + [sub_str], text[~i:], answer)



def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'enumerate_palindromic_decompositions.py',
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
