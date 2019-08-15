from test_framework import generic_test


def plus_one(A):
    if len(A) == 0:
        return A
    i = len(A)-1
    carry = 0
    remainder = True
    while(remainder and i >= 0):
        back = A[i]
        if(back < 9):
            if(carry):
                back += carry
                carry = 0
            else:
                back += 1
            A[i] = back
            remainder = False
        else:
            A[i] = 0
            carry = 1
        i = i-1

    if remainder:
        A.insert(0, 1)

    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
