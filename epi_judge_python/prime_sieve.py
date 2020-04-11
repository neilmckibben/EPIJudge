from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    if n is 0 or n is 1:
        return []
    if n is 2:
        return [2]
    primes = list(range(2, n + 1))
    for i in range(2, len(primes)):
        if primes[i-2]:
            j = 2
            val = i * j
            while val <= n:
                primes[val-2] = 0
                j += 1
                val = i * j
        i += 1
    return [x for x in primes if x is not 0]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
