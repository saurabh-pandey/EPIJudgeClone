from typing import List

from test_framework import generic_test
from tests.test_int_as_array_increment import TestIntAsArrayIncrement

def plus_one_v1(A: List[int]) -> List[int]:
    '''
    My O(n) version
    '''
    res = []
    carry = 1
    for a in reversed(A):
        if carry:
            if a != 9:
                res.append(a + 1)
                carry = 0
            else:
                res.append(0)
                carry = 1
        else:
            res.append(a)
    if carry:
        res.append(carry)
    res.reverse()
    return res

def plus_one_v2(A: List[int]) -> List[int]:
    '''
    Book's in place O(n) version
    '''
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    else:
        if A[0] == 10:
            A[0] = 1
            A.append(0)
    return A

def plus_one(A: List[int]) -> List[int]:
    # return plus_one_v1(A)
    return plus_one_v2(A)


if __name__ == '__main__':
    TestIntAsArrayIncrement(plus_one_v1).run_tests()
    TestIntAsArrayIncrement(plus_one_v2).run_tests()
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
