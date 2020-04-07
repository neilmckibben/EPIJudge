from test_framework import generic_test
from list_node import ListNode

def add_two_numbers(L1, L2):
    l1_size, l2_size, prev, iterator, carry = length(L1), length(L2), None, L1, 0
    if l1_size < l2_size:
        iterator = L2
    head = iterator
    while L1 and L2:
        value = (L1.data + L2.data + carry)
        if value > 9:
            carry = 1
            value -= 10
        else:
            carry = 0
        L1, L2 = L1.next, L2.next
        iterator.data = value
        prev = iterator
        iterator = iterator.next

    if carry != 0:
        while iterator:
            if iterator.data + 1 <= 9:
                iterator.data += 1
                break
            elif iterator.data + 1 == 10:
                iterator.data = 0
            prev = iterator
            iterator = iterator.next
        if not iterator:
            prev.next = ListNode(1)


    # while iterator:
    #     value = (iterator.data + carry)
    #     if value > 9:
    #         carry = 1
    #         value -= 10
    #     else:
    #         carry = 0
    #     sum += (value * (10 ** power))
    #     power += 1
    #     iterator = iterator.next

    return head

def length(head):
    head, size = head, 0
    while head:
        size += 1
        head = head.next
    return size


def reverse_list(head):
    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_list_add.py",
                                       'int_as_list_add.tsv', add_two_numbers))
