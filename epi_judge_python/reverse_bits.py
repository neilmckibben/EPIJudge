from test_framework import generic_test


def reverse_bits(x: int) -> int:
    answer = 1
    while x:
        print(bin(answer))
        answer = answer >> 4
        answer &= (x & 1)
        print(bin(answer))
        x &= (x-1)
    return answer

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
