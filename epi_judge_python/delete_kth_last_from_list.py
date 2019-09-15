from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    head = L
    super_front = L
    for i in range(0, k):
        super_front = super_front.next
    prev = None
    while super_front is not None:
        prev = L
        super_front = super_front.next
        L = L.next
    prev = L.next
    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
