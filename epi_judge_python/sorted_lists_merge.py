from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummyHead  = dummy
    L1Dummy = L1
    L2Dummy = L2
    while L1Dummy is not None or L2Dummy is not None:
        if L1Dummy is None:
            dummy.next = L2Dummy
            L2Dummy = L2Dummy.next
        elif L2Dummy is None:
            dummy.next = L1Dummy
            L1Dummy = L1Dummy.next
        else:
            if L1Dummy.data < L2Dummy.data:
                dummy.next = L1Dummy
                L1Dummy = L1Dummy.next
            else:
                dummy.next = L2Dummy
                L2Dummy = L2Dummy.next
        dummy = dummy.next
    return dummyHead.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
