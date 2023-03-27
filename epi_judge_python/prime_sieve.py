from typing import List

from test_framework import generic_test
from tests.test_prime_sieve import TestEnumeratePrimes

import math

def is_prime(n) -> bool:
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, math.floor(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
    return True

def generate_primes_v1(n: int) -> List[int]:
    '''
    O(n^3/2) basic version
    '''
    primes = []
    for i in range(1, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    # TODO - you fill in here.
    return []


if __name__ == '__main__':
    TestEnumeratePrimes(generate_primes_v1).run_tests()
    # exit(
    #     generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
    #                                    generate_primes))
