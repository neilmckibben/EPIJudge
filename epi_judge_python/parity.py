from test_framework import generic_test


def parity(x):
    count = 0
    while x:
        count ^= 1
        x &= (x - 1)
    return count

    # while x:
    #     print(x >> 2)
    #     x = x >> 2
    # return -1



# def parity_with_lookup(x):
#     # lookup = {01 : 1, 11 : 2, 10 : 1, 00 : 0}

if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
