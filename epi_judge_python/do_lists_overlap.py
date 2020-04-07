import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def length(head):
    start = head
    length = 0
    while head and start is not head:
        head = head.next
        length += 1
    return length



def overlapping_lists(l0, l1):
    return answer(l0, l1)
    # l0_length = length(l0)
    # l1_length = length(l1)
    # slow, fast = l0, l1
    # if l1_length < l0_length:
    #     slow, fast = l1, l0
    # while slow is not None and fast is not None and fast.next is not None and fast.next.next is not None:
    #     fast = fast.next
    #     fast = fast.next
    #     slow = slow.next
    #     if fast is slow:
    #         return fast
    return None


def answer(l0, l1):
    root0, root1 = has_



@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_lists_overlap.py",
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
