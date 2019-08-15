from test_framework import generic_test


def multiply(num1, num2):
    sum = list()
    indexOne = len(num1)-1
    indexTwo = len(num2)-1
    carry = 0
    overFlow = False
    while((indexOne >= 0) or (indexTwo >= 0)):
        backOne = num1[indexOne]
        backTwo = num2[indexTwo]

        product = (backOne * backTwo) + carry
        if(product > 9):
            carry = product/10
        else:
            carry = 0
        sum.append(product)

    return sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))
