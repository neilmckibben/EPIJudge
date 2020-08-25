import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    def length(head):
        len = 0
        while head:
            head = head.next
            len += 1
        return len

    def validate(one, two):
        while one and two:
            if one.data != two.data:
                return False
            one = one.next
            two = two.next
        return one is None and two is None

    l0_length, l1_length = length(l0), length(l1)

    long, short = l0, l1

    if l1_length > l0_length:
        long, short = l1, l0
    offset = max(l0_length,  l1_length) - min(l0_length, l1_length)
    i = 0
    while i < offset:
        long = long.next
        i += 1
    while long:
        if long.data == short.data and validate(long, short):
            return long
        long = long.next
        short = short.next
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

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
