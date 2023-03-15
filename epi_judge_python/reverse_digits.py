from test_framework import generic_test
from tests.test_reverse_digits import TestReverseDigits

import math

def reverse_v1(x: int) -> int:
    '''
    Brute force version O(n)
    '''
    if x == 0:
        return 0
    result = abs(x)
    num_digits = math.floor(math.log10(result)) + 1
    digits = [0 for i in range(num_digits)]
    for i in range(num_digits, 0, -1):
        power = 10 ** (i - 1)
        digits[num_digits - i] = result // power
        result -= power * digits[num_digits - i]
    i = 0
    j = num_digits - 1
    while i < j:
        temp = digits[i]
        digits[i] = digits[j]
        digits[j] = temp
        i += 1
        j -= 1
    result = 0
    power = 10 ** (num_digits - 1)
    for d in digits:
        result += power * d
        power //= 10
    return -result if x < 0 else result

def reverse_v2(x: int) -> int:
    '''
    Book's O(n) version
    '''
    result = 0
    remaining_digits = abs(x)
    while remaining_digits:
        result = result * 10 + remaining_digits % 10
        remaining_digits //= 10
    return -result if x < 0 else result

def reverse(x: int) -> int:
    # return reverse_v1(x)
    return reverse_v2(x)


if __name__ == '__main__':
    TestReverseDigits(reverse_v1).run_tests()
    TestReverseDigits(reverse_v2).run_tests()
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
