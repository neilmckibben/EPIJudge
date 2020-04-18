from typing import List

from test_framework import generic_test


def get_valid_ip_address(s: str) -> List[str]:
    if len(s) < 4:
        return []
    ip_adresses = list()
    i = 0
    one = s[~i]
    while int(one) <= 256 and i < len(s):
        j = i + 1
        two = s[~j]
        while int(two) <= 256 and j < len(s):
            k = j + 1
            three = s[~k]
            while int(three) <= 256 and k < len(s):
                n = k + 1
                four = s[~n]
                while int(four) <= 256 and n < len(s):
                    ip = str(four) + "." + str(three) + "." + str(two) + "." + str(one) + "."
                    ip_adresses.append(ip)
                    n += 1
                    four = s[~n]

                k += 1
                three += s[~k]
        j += 1
        two += s[~j]


        i += 1
        one += s[~i]

    return ip_adresses


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
