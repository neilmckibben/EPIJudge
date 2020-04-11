from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    head = L
    length = 0
    while head:
        length += 1
        head = head.next
    front, back = L, L
    middle = length // 2
    for i in range(0, middle):
        back = back.next
    while back:
        if front is not back:
            return False
        front, back = front.next, back.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
