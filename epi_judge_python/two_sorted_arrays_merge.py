from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    #Avoid moving entries by sorting from the back -> forwards
    back_A = m - 1
    back_B = len(B) - 1
    back = len(A) - 1
    while back_B >= 0 and back_A >= 0:
        if B[back_B] >= A[back_A]:
            A[back] = B[back_B]
            back_B -= 1
        elif B[back_B] < A[back_A]:
            A[back] = A[back_A]
            back_A -= 1
        back -= 1
    #We finish but some array has some min values
    #Iterate over the front
    back = 0
    if back_B >= 0:
        while back < back_B + 1:
            A[back] = B[back]
            back += 1

    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
