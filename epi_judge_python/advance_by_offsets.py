from time import sleep

from test_framework import generic_test


def can_reach_end(A):
    if len(A) == 1:
        return True
    max_attainable = A[0]
    i = 1
    while i <= max_attainable:
        if A[i] + i >= len(A) - 1:
            return True
        increase = (A[i] + i - max_attainable)
        if increase > 0:
            max_attainable += (A[i] + i - max_attainable)
        i += 1
    return False


# def evaluate(A, start, length):
#     value = False
#     if (len(A) - 1) == start:
#         return True
#     for i in range(start + 1, length + start + 1):
#         if evaluate(A, i, A[i]):
#             return True
#     return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
