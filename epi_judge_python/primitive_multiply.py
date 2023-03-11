from test_framework import generic_test
from tests.test_primitive_multiply import TestPrimitiveMultiply

import pdb

def add_primitive(x: int, y: int) -> int:
    # pdb.set_trace()
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
    return sum(additives)

def multiply(x: int, y: int) -> int:
    # TODO - you fill in here.
    return 0


if __name__ == '__main__':
    # print(f"### {1} + {3} = {add_primitive(1, 3)}")
    # print(f"### {2} + {3} = {add_primitive(2, 3)}")
    # print(f"### {5} + {4} = {add_primitive(5, 4)}")
    # print(f"### {0} + {1} = {add_primitive(0, 1)}")
    # print(f"### {1} + {0} = {add_primitive(1, 0)}")
    # print(f"### {21} + {9} = {add_primitive(21, 9)}")
    for x in range(20):
        for y in range(20):
            print(f"### {x} + {y} = {add_primitive(x, y)}")
            assert add_primitive(x, y) == (x + y), f"Failed for {x} + {y}"
    TestPrimitiveMultiply(multiply_v1).run_tests()
    # exit(
    #     generic_test.generic_test_main('primitive_multiply.py',
    #                                    'primitive_multiply.tsv', multiply))
