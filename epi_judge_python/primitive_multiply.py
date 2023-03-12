from test_framework import generic_test
from tests.test_primitive_multiply import (TestPrimitiveMultiply,
    TestPrimitiveAddition)

def add_primitive(x: int, y: int) -> int:
    sum = 0
    carry = 0
    i = 0
    while x | y:
        bit1 = x & 1
        bit2 = y & 1
        bit_sum = bit1 ^ bit2
        bit_sum ^= carry
        carry = (bit1 & bit2) | (carry & bit1) | (carry & bit2)
        sum |= (bit_sum << i)
        x >>= 1
        y >>= 1
        i += 1
    sum |= (carry << i)
    return sum

def multiply_v1(x: int, y: int) -> int:
    '''
    O(n^2) version
    '''
    additives = []
    while x:
        if x & 1:
            additives.append(y)
        y <<= 1
        x >>= 1
    product = 0
    if additives:
        product = additives[0]
        for rest_add in additives[1:]:
            product = add_primitive(product, rest_add)
    return product

def multiply_v2(x: int, y: int) -> int:
    '''
    Book's fantastic O(n^2) solution
    '''
    def add(a: int, b: int) -> int:
        return a if b == 0 else add(a ^ b, (a & b) << 1)
    
    running_sum = 0
    while x:
        if x & 1:
            running_sum = add(running_sum, y)
        x, y = x >> 1, y << 1
    return running_sum

def multiply(x: int, y: int) -> int:
    return multiply_v2(x, y)


if __name__ == '__main__':
    TestPrimitiveAddition(add_primitive).run_tests()
    TestPrimitiveMultiply(multiply_v1).run_tests()
    TestPrimitiveMultiply(multiply_v2).run_tests()
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
