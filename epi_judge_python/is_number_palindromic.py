from test_framework import generic_test
from tests.test_is_number_palindromic import TestIsNumberPalindromic

import math

def is_palindrome_number_v1(x: int) -> bool:
    '''
    Basic O(n) time and space solution
    '''
    if x <= 0:
        return x == 0
    num_digits = math.floor(math.log10(x)) + 1
    digits = [0 for _ in range(num_digits)]
    for i in range(num_digits):
        digits[i] = x % 10
        x //= 10
    i = 0
    j = num_digits - 1
    while i < j:
        if digits[i] != digits[j]:
            return False
        i += 1
        j -= 1
    return True

def is_palindrome_number(x: int) -> bool:
    return is_palindrome_number_v1(x)


if __name__ == '__main__':
    TestIsNumberPalindromic(is_palindrome_number_v1).run_tests()
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
