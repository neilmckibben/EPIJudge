from test_framework import generic_test


def remove_duplicates(L):
    head = L
    current = L
    check = -1
    prev = current
    while current is not None:
        current_val = current.data
        if current_val == check:
            prev.next = current.next
        else:
            prev = current
        check = current_val

        current = current.next
    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "remove_duplicates_from_sorted_list.py",
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
