from test_framework import generic_test

from typing import List


def parity_v1(x: int) -> int:
    '''
    O(n) runtime solution where n is number of bits in x
    '''
    p = 0
    while x:
        p ^= (x & 1)
        x >>= 1
    return p

def parity_v2(x: int) -> int:
    '''
    O(k) solution where k is number of bits set to 1
    '''
    p = 0
    while x:
        p ^= 1
        x &= (x - 1)
    return p


def fill_cache(cache_size: int) -> List[int]:
    max_val = 1 << cache_size
    parity_cache = [0 for _ in range(max_val)]
    for n, _ in enumerate(parity_cache):
        parity_cache[n] = parity_v2(n)
    return parity_cache

def parity_v3(x: int, parity_cache: List[int]) -> int:
    '''
    O(n/cache_bits_size) version with an inital pre-filled cache of parity
    '''
    mask = 0xFFFF
    p1 = parity_cache[x & mask]
    p2 = parity_cache[(x >> 16) & mask]
    p3 = parity_cache[(x >> 32) & mask]
    p4 = parity_cache[(x >> 48)]
    return p1 ^ p2 ^ p3 ^ p4


# PARITY_CACHE = fill_cache(16)

def parity_v4(x: int) -> int:
    '''
    O(log n) version
    '''
    p1 = x ^ (x >> 32)
    p2 = p1 ^ (p1 >> 16)
    p3 = p2 ^ (p2 >> 8)
    p4 = p3 ^ (p3 >> 4)
    p5 = p4 ^ (p4 >> 2)
    p6 = p5 ^ (p5 >> 1)
    return p6 & 0x1

def parity(x: int) -> int:
    # res = parity_v1(x)
    # res = parity_v2(x)
    # res = parity_v3(x, PARITY_CACHE)
    res = parity_v4(x)
    return res


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
