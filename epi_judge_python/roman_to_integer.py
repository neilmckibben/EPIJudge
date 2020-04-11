from test_framework import generic_test


def roman_to_integer(s: str) -> int:
    val = 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if len(s) is 1:
        return roman[s[0]]
    maximum = -1
    for i in range(0, len(s)):
        value = roman[s[~i]]
        if value < maximum:
            val -= value
        else:
            val += value
        maximum = max(value, maximum)
    return val
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
