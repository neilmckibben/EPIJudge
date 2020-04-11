from test_framework import generic_test


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    # wanna convert it to base 10 then back????
    return_value = str()
    digit_power = 0
    #convert to base 10
    while num_as_string:
        digit = int((num_as_string[-1]))
        raw_digit = digit (b1)
        new_digit = raw_digit * (b2 ** digit_power)
        return_value += str(new_digit)
        num_as_string = num_as_string[:-1]
        digit_power += 1

    return return_value[::-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
