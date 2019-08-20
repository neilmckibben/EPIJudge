from test_framework import generic_test


def roman_to_integer(s):
    val = 0
    keyDict = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    length = len(s)-2
    val += keyDict[s[-1]]
    while length >= 0:
        current = s[length]
        currentInt = keyDict[current]
        back = s[length+1]
        backInt = keyDict[back]
        if(backInt > currentInt):
            val = val - currentInt
        else:
            val += currentInt
        length = length-1

    return val



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "roman_to_integer.py", 'roman_to_integer.tsv', roman_to_integer))
