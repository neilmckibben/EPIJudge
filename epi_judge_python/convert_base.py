from test_framework import generic_test

conversion = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11,
              "C": 12, "D": 13, "E": 14, "F": 15}
str_conversion = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B",
                  12: "C", 13: "D", 14: "E", 15: "F"}


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    answer = ""
    sum = 0
    if num_as_string[0] == "-":
        num_as_string = num_as_string[1:]
        answer += "-"
    for i in range(0, len(num_as_string)):
        number = conversion[num_as_string[~i]]
        power = (b1 ** i)
        sum += number * power
    i = 0
    while b2 ** i <= sum:
        i += 1
    max_power = i - 1
    if sum is 0:
        return "0"
    while max_power != 0:
        value = b2 ** max_power
        digit = sum // value
        sum -= digit * value
        answer += str_conversion[digit]
        max_power -= 1
    return answer + str_conversion[sum]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
