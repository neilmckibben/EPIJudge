from test_framework import generic_test


def cyclically_right_shift_list(L, k):
    front, back, i, new_front, length = L, L, L, None, 0
    while i:
        i = i.next
        length += 1
    if length < 2:
        return L
    shift = k % length
    if shift == 0:
        return L
    for i in range(0, shift):
        front = front.next
    while front.next:
        front, back = front.next, back.next
    new_front = back.next
    back.next = None
    front.next = L
    return new_front


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("list_cyclic_right_shift.py",
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
