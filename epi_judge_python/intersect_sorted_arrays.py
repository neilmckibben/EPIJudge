from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    short, long = A, B
    if len(B) < len(A):
        short, long = B, A
    s_index, l_index = 0, 0
    intersection = []
    while s_index < len(short) and l_index < len(long):
        if short[s_index] == long[l_index]:
            val = short[s_index]
            intersection.append(short[s_index])
            while s_index < len(short) and val == short[s_index]:
                s_index += 1
            while l_index < len(long) and val == long[l_index]:
                l_index += 1
        elif long[l_index] < short[s_index]:
            while l_index < len(long) and long[l_index] < short[s_index]:
                l_index += 1
        else:
            s_index += 1
    return intersection


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
