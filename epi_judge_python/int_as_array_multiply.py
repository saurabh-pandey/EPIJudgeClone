from typing import List

from test_framework import generic_test
from tests.test_int_as_array_multiply import (
    TestIntAsArrayMultiply,
    TestIntAsArrayAdd
)


def add(num1: List[int], num2: List[int]) -> List[int]:
    '''
    O(n) add two nums as arrays
    '''
    sz1 = len(num1)
    sz2 = len(num2)
    larger_num = num2[:] if sz2 > sz1 else num1[:]
    smaller_num = num1[:] if sz2 > sz1 else num2[:]
    i = len(larger_num) - 1
    j = len(smaller_num) - 1
    carry = 0
    while i >= 0:
        if j < 0:
            digit_sum = larger_num[i] + carry
            larger_num[i] = digit_sum % 10
            carry = digit_sum // 10
        else: # i >=0 and j >= 0
            digit_sum = larger_num[i] + smaller_num[j] + carry
            larger_num[i] = digit_sum % 10
            carry = digit_sum // 10
        i -= 1
        j -= 1
    if carry:
        larger_num.append(0)
        for i in reversed(range(1, len(larger_num))):
            larger_num[i] = larger_num[i - 1]
        larger_num[0] = 1
    return larger_num

def multiply(num1: List[int], num2: List[int]) -> List[int]:
    # TODO - you fill in here.
    return []


if __name__ == '__main__':
    TestIntAsArrayAdd(add).run_tests()
    # exit(
    #     generic_test.generic_test_main('int_as_array_multiply.py',
    #                                    'int_as_array_multiply.tsv', multiply))
