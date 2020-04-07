from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    front, back, head = L, L, L
    for i in range(0, k + 1):
        if not front:
            return head.next
        front = front.next
    while front:
        front = front.next
        back = back.next
    back.next = back.next.next
    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
