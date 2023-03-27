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

def generate_primes_v2(n: int) -> List[int]:
    '''
    Sieve version of the algorithm
    '''
    primes = []
    # is_prime is true for all primes s.t. for every prime p is_prime[p - 1]
    # should be true otherwise false
    is_prime = [True for _ in range(n)]
    is_prime[0] = False # 1 is not prime
    for i in range(2, n + 1):
        if is_prime[i - 1]:
            primes.append(i)
            for multiple in range(2 * i, n + 1, i):
                is_prime[multiple - 1] = False
    return primes

def generate_primes_v3(n: int) -> List[int]:
    '''
    Books much more optimized sieve version
    '''
    if n < 2:
        return []
    primes = [2]
    sz = ((n - 3) // 2) + 1
    # For each i in is_prime the prime number it represents is 2 * i + 3
    is_prime = [True] * sz
    for i in range(sz):
        if is_prime[i]:
            p = 2 * i + 3
            primes.append(p)
            for j in range(2 * i**2 + 6 * i + 3, sz, p):
                is_prime[j] = False
    return primes



# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    # return generate_primes_v2(n)
    return generate_primes_v3(n)


if __name__ == '__main__':
    TestEnumeratePrimes(generate_primes_v1).run_tests()
    TestEnumeratePrimes(generate_primes_v2).run_tests()
    TestEnumeratePrimes(generate_primes_v3).run_tests()
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
