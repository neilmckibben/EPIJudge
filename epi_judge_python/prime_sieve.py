from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n):
    primes = list()
    if n < 2:
        return []
    elif n == 2:
        return [2]
    valid = list()
    count = 0
    while count < n:
        valid.append(True)
        count += 1

    valid[0] = False
    valid[1] = False

    for i in valid:
        if valid:
            range(valid, i)

    for i in range(0, len(valid)):
        if valid:
            primes.add(i)


    return
'''
    valid[0] = False

    for v in range(3, len(valid)):
        if valid[2] is True:
            primes.append()
        i += 1
'''


def range(valid, factor):
    multiplier = 2
    while (factor * multiplier) < valid[-1]:
        valid[factor * multiplier] = False
        multiplier = multiplier + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv",
                                       generate_primes))
