import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def list_pivoting(l, x):
    less_than, equal_to, greater_than = ListNode(0), ListNode(0), ListNode(0)
    dummy_less, dummy_equal, dummy_greater = less_than, equal_to, greater_than

    while l:
        if l.data < x:
            less_than.next = l
            less_than = less_than.next
        elif l.data == x:
            equal_to.next = l
            equal_to = equal_to.next
        else:
            greater_than.next = l
            greater_than = greater_than.next
        l = l.next
    greater_than.next = None
    equal_to.next = dummy_greater.next
    less_than.next = dummy_equal.next
    return dummy_less.next


def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("pivot_list.py", 'pivot_list.tsv',
                                       list_pivoting_wrapper))
