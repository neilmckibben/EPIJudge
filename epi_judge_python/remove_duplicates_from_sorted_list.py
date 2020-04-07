from test_framework import generic_test

def remove_duplicates(L):
    head = L
    current_node = None
    current_value = None
    while head:
        if head.data != current_value:
            current_node, current_value = head, head.data
        else:
            forward = head
            while forward and forward.data == head.data:
                forward = forward.next
            current_node.next = forward
        head = current_node.next
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "remove_duplicates_from_sorted_list.py",
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
