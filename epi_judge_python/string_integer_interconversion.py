from test_framework import generic_test
from test_framework.test_failure import TestFailure

mapping_string = {1: "1", 0: "0", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
mapping_int = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}


def int_to_string(x: int) -> str:
    val = ""
    negative = ""
    if x is 0:
        return "0"
    if x < 0:
        negative = "-"
        x = x * -1
    while x:
        digit = x % 10
        val += mapping_string[digit]
        x = x // 10
    return negative + val[::-1]


def string_to_int(s: str) -> int:
    intVal = 0
    power = 0
    negative = 1
    while s:
        digit = s[-1]
        if digit != "-":
            if digit != "+":
                intVal += mapping_int[digit] * (10 ** power)
                power += 1
        else:
            negative = -1
        s = s[:-1]
    return intVal * negative


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
