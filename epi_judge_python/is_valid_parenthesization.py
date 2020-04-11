from test_framework import generic_test

expected = {")": "(", "]": "[", "}": "{"}

def is_well_formed(s: str) -> bool:
    tokens = list(s)
    stack = list()
    for token in tokens:
        if token in expected:
            if len(stack) == 0 or stack.pop() != expected[token]:
                return False
        else:
            stack.append(token)
    return len(stack) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
