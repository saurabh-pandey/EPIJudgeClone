from test_framework import generic_test
from test_framework.test_failure import TestFailure
from tests.test_string_integer_interconversion import(
    TestIntegerToStringConversion, TestStringToIntegerConversion
)


def int_to_string_v1(x: int) -> str:
    '''
    My O(n) time and space version
    '''
    if x == 0:
        return "0"
    s = []
    sign = -1 if x < 0 else 1
    x = sign * x
    while x:
        s.append(str(x % 10))
        x //= 10
    if sign == -1:
        s.append("-")
    s.reverse()
    return ''.join(s)

def int_to_string(x: int) -> str:
    return int_to_string_v1(x)


def string_to_int_v1(s: str) -> int:
    '''
    My O(n) space and time version
    '''
    n = 0
    sign = 1
    sz = len(s)
    i = 0
    if s[0] == "-":
        sign = -1
        sz -= 1
        i = 1
    elif s[0] == "+":
        sign = 1
        sz -= 1
        i = 1
    for c in s[i:]:
        d = int(c)
        n += d * 10 ** (sz - 1)
        sz -= 1
    return sign * n

def string_to_int(s: str) -> int:
    return string_to_int_v1(s)


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    TestIntegerToStringConversion(int_to_string_v1).run_tests()
    TestStringToIntegerConversion(string_to_int_v1).run_tests()
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
