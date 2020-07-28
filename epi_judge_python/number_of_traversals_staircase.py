from test_framework import generic_test


def number_of_ways_to_top(top: int, maximum_step: int) -> int:
    steps = [0] * top

    # def calculate_step(value):
    #     if steps[value - 1] == -1:
    #         i = 0
    #         while i < maximum_step:
    #             factor = i + 1
    #             if value % factor == 0:
    #                 if steps[value - 1] == -1:
    #                     steps[value-1] = 1
    #                 else:
    #                     steps[value - 1] += 1
    #             elif factor < value:
    #                 steps[value-1] += 2 * calculate_step(value - factor)
    #             i += 1
    #     return steps[value - 1]

    def calculate_step(value):
        if steps[value - 1] == 0:
            i = 0
            while i < maximum_step:
                factor = i + 1
                if value == factor:
                    steps[value - 1] += 1
                if value - factor > 0:
                    steps[value - 1] += calculate_step(value - factor)
                i += 1
        return steps[value - 1]

    for i in range(0, top):
        calculate_step(i + 1)
    return steps[-1]


# 2, 3
# 1 + 1 + 1 + 1
# 2 + 2
# 2 + 1 + 1
# 1 + 2 + 1
# 1 + 1 + 2


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_staircase.py',
                                       'number_of_traversals_staircase.tsv',
                                       number_of_ways_to_top))
