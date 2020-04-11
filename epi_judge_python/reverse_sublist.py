from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    head, i, before_reverse = L, 1, None

    while i < start:
        before_reverse = L
        L = L.next
        i += 1

    node = reverse(L, start, finish)
        if before_reverse:
            before_reverse.next = node
        else:
            head = node

    return head


def reverse(head, start, finish):
    prev, temp = None, None
    copy = head

    while head is not None and start < finish + 1:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
        start += 1
    if copy:
        copy.next = temp

    return prev

        return head

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
