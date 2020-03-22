import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(A):
    valid_elements = 0
    i = 0
    prev = None
    while i < len(A):
        if A[i] != prev:
            A[valid_elements] = A[i]
            valid_elements += 1
        prev = A[i]
        i += 1
    return valid_elements
#breaks @12 for TC 1

@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_array_remove_dups.py",
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
