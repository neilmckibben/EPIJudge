from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L):
    print(L)
    if L is not None:
        current = L
        even = ListNode()
        evenHead = even
        odd = ListNode()
        oddHead = odd
        counter = 0
        while current is not None:
            if counter % 2 == 0:
                even.next = current
                even = even.next
            else:
                odd.next = current
                odd = odd.next
            current = current.next
            counter += 1

        even.next = oddHead.next
        odd.next = None
        return evenHead.next
    return None

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
