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

def multiply_v1(num1: List[int], num2: List[int]) -> List[int]:
    '''
    My O(n^2) version
    '''
    sign = -1 if (num1[0] * num2[0]) < 0 else 1
    number1 = num1[:]
    number2 = num2[:]
    number1[0] = abs(number1[0])
    number2[0] = abs(number2[0])
    running_sum = []
    for i, n1 in enumerate(reversed(number1)):
        product = [0 for _ in range(i)]
        carry = 0
        for n2 in reversed(number2):
            mult = n1 * n2 + carry
            product.append(mult % 10)
            carry = mult // 10
        if carry:
            product.append(carry)
        product.reverse()
        if not running_sum:
            running_sum = [0 for _ in product]
        running_sum = add(running_sum, product)
    running_sum[0] *= sign
    if all(n == 0 for n in running_sum):
        running_sum = [0]
    return running_sum

def multiply(num1: List[int], num2: List[int]) -> List[int]:
    return multiply_v1(num1, num2)


if __name__ == '__main__':
    TestIntAsArrayAdd(add).run_tests()
    TestIntAsArrayMultiply(multiply_v1).run_tests()
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
