import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0, l1):
    #See if the last node is the same
    temp_l0 = l0
    prev_l0 = l0
    while temp_l0 is not None:
        prev_l0 = temp_l0
        temp_l0 = temp_l0.next

    temp_l1 = l1
    prev_l1 = l1
    while temp_l1 is not None:
        prev_l1 = temp_l1
        temp_l1 = temp_l1.next

    if prev_l0 is prev_l1:
        while





    return None


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(
        functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_terminated_lists_overlap.py",
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
