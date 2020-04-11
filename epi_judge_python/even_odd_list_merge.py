from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if L is None:
        return None
    odd, even = ListNode(0), ListNode(0)
    head_even, head_odd = even, odd
    index = 0
    while L:
        if index % 2 == 0:
            even.next = L
            even = even.next
        else:
            odd.next = L
            odd = odd.next
        L = L.next
        index += 1
    odd.next = None
    even.next = head_odd.next
    return head_even.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
