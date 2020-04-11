from test_framework import generic_test


def swap_bits(x, i, j):
    counter = 1
    bit_one = -1
    bit_two = -1
    dummy = x
    print("\nBefore swap: ", bin(x))
    while counter < max(i, j) + 1:
        print(dummy & 1)
        if counter is i:
            bit_one = (dummy & 1)
        if counter is j:
            bit_two = (dummy & 1)
        dummy &= (dummy - 1)
        counter += 1
    print(bit_one, bit_two)
    if bit_one == bit_two:
        return x
    if bit_one:
        x = (x | (2**j))
    else:
        x = (x ^ (2**j))

    if bit_two:
        x = (x | (2**i))
    else:
        x = (x ^ (2**i))
    print("After swap: ", bin(x), " with index ", i, " and ", j, " swapped")
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
