from typing import List

from test_framework import generic_test


def get_valid_ip_address(s: str) -> List[str]:
    if len(s) < 4:
        return []
    ip_adresses = list()
    i = 1
    while i < len(s) and int(s[:i]) <= 256:
        str_one = s[:i]
        one = int(str_one)
        j = i + 1
        while j < len(s) and int(s[i:j]) <= 256:
            str_two = s[i:j]
            two = int(str_two)
            k = j + 1
            while k < len(s) and int(s[j:k]) <= 256:
                str_three = s[j:k]
                three = int(str_three)
                l = k
                str_four = s[l:]
                four = int(str_four)
                #Check for leading 0's somehow
                if four <= 256:
                    #Assume valid
                    ip_address = str_one + "." + str_two + "." + str_three + "." + str_four
                    invalid = False
                    for n in range(0, len(ip_address) - 1):
                        fast = n + 1
                        if ip_address[n] == "0" and ip_address[fast] == "0":
                            invalid = True
                    if not invalid and ip_address not in ip_adresses:
                        ip_adresses.append(ip_address)

                k += 1
            j += 1
        i += 1

    return ip_adresses


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
