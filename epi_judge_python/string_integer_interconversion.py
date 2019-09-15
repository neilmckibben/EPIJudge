from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
    val = ""
    if x is 0:
        return "0"

    while x is not 0:
        digit = chr(x % 10)
        val += digit
        x = x/10
    return val.reverse()


def string_to_int(s):
    intVal = 0
    digitCount = 0
    negative = False
    if s[0] is "-":
        negative = True
        s = s[1:]
    if s is "0":
        return 0
    while not s:
        digit = int(s[-1]) #get back digit
        digit = (10**digitCount) + digit #raise it to a power
        s = s[:-1] #remove the last
        intVal += digit
        digitCount += 1 #higher power
    return intVal


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
