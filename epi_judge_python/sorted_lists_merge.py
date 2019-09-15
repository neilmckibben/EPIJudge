from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1, L2):
    dummy = ListNode()
    head = dummy
    while L1 is not None and L2 is not None:
        l1_val = L1.data
        l2_val = L2.data
        min = None
        if l1_val < l2_val:
            min = L1
            L1 = L1.next
        else:
            min = L2
            L2 = L2.next
        dummy.next = min
        dummy = dummy.next

    if L1 is None:
        dummy.next = L2
    else:
        dummy.next = L1

    return head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
