import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index, A):
    pivotValue = A[pivot_index]
    leftIndex = 0
    rightIndex = pivot_index
    for i in range(0, len(A)):
        check = A[i]
        if i is not pivot_index:
            if (leftIndex < pivot_index) and (rightIndex < len(A)):
                if check > pivotValue:
                    swap(A, i, rightIndex)
                    leftIndex += 1
                elif check < pivotValue:
                    swap(A, i, leftIndex)
                    rightIndex += 1
            else:
                return
    return


def swap(A, indexOne, indexTwo):
    temp = A[indexOne]
    A[indexOne] = A[indexTwo]
    A[indexTwo] = temp


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("dutch_national_flag.py",
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
