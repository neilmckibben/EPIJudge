from test_framework import generic_test


def examine_buildings_with_sunset(sequence):
    if len(sequence) == 0:
        return []
    max_height = sequence[-1]
    sunset = [len(sequence) - 1]
    for i in range(1, len(sequence)):
        building = sequence[~i]
        if building > max_height:
            sunset.append(len(sequence) - 1 - i)
            max_height = building
    return sunset


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sunset_view.py", 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
