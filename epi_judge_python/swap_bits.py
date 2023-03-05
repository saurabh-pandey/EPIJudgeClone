from test_framework import generic_test
from tests import test_swap_bits

def clear_bit(n: int) -> int:
    cleared_bit_n = 0
    for i in range(64):
        if i != n:
            cleared_bit_n |= (1 << i)
    return cleared_bit_n


def swap_bits_v1(x, i, j):
    '''
    My original solution O(n)
    '''
    i_bit = x & (1 << i)
    j_bit = x & (1 << j)
    if i_bit and not j_bit:
        i_bit_cleared = clear_bit(i)
        x &= i_bit_cleared
        x |= (1 << j)
    elif not i_bit and j_bit:
        j_bit_cleared = clear_bit(j)
        x &= j_bit_cleared
        x |= (1 << i)
    return x

def swap_bits_v2(x, i, j):
    '''
    Books O(1) solution
    '''
    if ((x >> i) & 1) != ((x >> j) & 1):
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x

def swap_bits(x, i, j):
    return swap_bits_v2(x, i, j)

if __name__ == '__main__':
    test_swap_bits.TestSwapBits(swap_bits_v1, "My Swap bits").run_tests()
    test_swap_bits.TestSwapBits(swap_bits_v2, "Book Swap bits").run_tests()
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
