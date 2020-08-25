from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s: str) -> str:
    i = 0
    decoded = ""
    while i < len(s):
        character = s[i]
        if character.isdigit():
            digit = s[i]
            i += 1
            # Expand to get all the digits
            while i < len(s) and s[i].isdigit():
                digit += s[i]
                i += 1
            character = s[i]
            decoded += character * int(digit)
            i += 1
    return decoded


def encoding(s: str) -> str:
    i = 0
    encoded = ""
    while i < len(s):
        character = s[i]
        count = 1
        i += 1
        while i < len(s) and s[i] == character:
            count += 1
            i += 1
        encoded += str(count) + character
    return encoded


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))
