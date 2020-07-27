from typing import List

from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    if num_pairs == 0:
        return ['']
    answer = []
    generate("", num_pairs, answer, 0, 0)

    return sorted(answer)

def generate(path, num_pairs, answer, left, right):
    if num_pairs == 0:
        if path not in answer and left == right:
            answer.append(path)
        return
    path += "("
    left += 1
    diff = left - right
    i = 0
    right_paren = ""
    while i <= diff:
        generate(path + right_paren, num_pairs - 1,  answer, left, right + i)
        right_paren += ")"
        i += 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_balanced_parentheses.py',
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
