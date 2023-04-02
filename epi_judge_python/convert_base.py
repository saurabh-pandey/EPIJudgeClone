from test_framework import generic_test
from tests.test_convert_base import TestConvertBase


to_int = {
    "0" : 0, "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7,
    "8" : 8, "9" : 9, "A" : 10, "B" : 11, "C" : 12, "D" : 13, "E" : 14, "F" : 15
}

to_digit = {
    0 : "0", 1 : "1", 2 : "2", 3 : "3", 4 : "4", 5 : "5", 6 : "6", 7 : "7",
    8 : "8", 9 : "9", 10 : "A", 11 : "B", 12 : "C", 13 : "D", 14 : "E", 15 : "F"
}

def convert_base_v1(num_as_str: str, b1: int, b2: int) -> str:
    '''
    My version
    '''
    num_in_decimal = 0
    sign = 1
    start = 0
    power = len(num_as_str) - 1
    if num_as_str[0] == "-":
        sign = -1
        start = 1
        power -= 1
    while start < len(num_as_str):
        num_in_decimal += to_int[num_as_str[start]] * (b1 ** (power))
        start += 1
        power -= 1
    
    if num_in_decimal == 0:
        return "0"
    
    num_in_new_base = []
    while num_in_decimal:
        new_digit = num_in_decimal % b2
        num_in_new_base.append(to_digit[new_digit])
        num_in_decimal //= b2
    if sign == -1:
        num_in_new_base.append("-")
    num_in_new_base.reverse()
    return "".join(num_in_new_base)

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    return convert_base_v1(num_as_string, b1, b2)


if __name__ == '__main__':
    TestConvertBase(convert_base_v1).run_tests()
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
