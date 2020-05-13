from test_framework import generic_test

#Palindrome conditions:
# All numbers are even or all are even and one thing is odd
def can_form_palindrome(s: str) -> bool:
    table = dict()
    for character in s:
        table[character] = table.get(character, 0) + 1
    odd_occurence = False
    for value in table.values():
        if value % 2 == 1:
            if odd_occurence:
                return False
            else:
                odd_occurence = True

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
