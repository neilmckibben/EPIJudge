from typing import List

from test_framework import generic_test, test_utils

mappings = ["0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

def phone_mnemonic(phone_number: str) -> List[str]:
    ans = []
    recurse(phone_number, "", ans)


    return ans

def recurse(number, path, ans):
    if number:
        char = number[0]
        vals = mappings[int(char)]
        for val in vals:
            recurse(number[1:], path + val, ans)
    elif path not in ans:
        ans.append(path)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
