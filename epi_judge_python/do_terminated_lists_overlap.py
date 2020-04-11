import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
def overlapping_no_cycle_lists(l0, l1):
    #See if the last node is the same
    l0_size = 0
    l0_dummy = l0
    l1_size = 0
    l1_dummy = l1
    offset = 0
    while l0_dummy:
        l0_dummy = l0_dummy.next
        l0_size += 1
    while l1_dummy:
        l1_dummy = l1_dummy.next
        l1_size += 1

    short, short_dummy = l1, l1
    long = l0
    offset = l0_size - l1_size
    if l0_size < l1_size:
        short, short_dummy, long = l0, l0, l1
        offset = l0_size - l1_size
    if l0_size == 1 and l0_size == 1:
        if l1 is l0:
            return l1
        return None
    elif l0_size == 1 or l1_size == 1:
        while long:
            if long is short:
                return long
            long = long.next
        return None


    iterator = 1
    while long:
        if offset < iterator:
            if short is long:
                return short
            short = short.next
        long = long.next
        iterator += 1
    return l0

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

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
