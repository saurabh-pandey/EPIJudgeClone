from tests.test_base import TestBase
from tests.utils import int_as_array

import pdb

class TestIntAsArrayAdd(TestBase):
    def test_example1(self):
        # pdb.set_trace()
        # num1 = int_as_array.convert(0)
        # num2 = int_as_array.convert(10)
        # expected = int_as_array.convert(0 + 10)
        # res = self.solve(num1, num2)
        # print(f"{num1} + {num2} = {expected}, res = {res}")
        for i in range(2000):
            num1 = int_as_array.convert(i)
            for j in range(2000):
                num2 = int_as_array.convert(j)
                expected = int_as_array.convert(i + j)
                # print(f"Starting add of {num1} + {num2}")
                res = self.solve(num1, num2)
                # print(f"{num1} + {num2} = {expected}, res = {res}")
                assert res == expected

class TestIntAsArrayMultiply(TestBase):
    def test_example1(self):
        for i in range(200):
            num1 = int_as_array.convert(i)
            for j in range(200):
                num2 = int_as_array.convert(j)
                expected = int_as_array.convert(i * j)
                assert self.solve(num1, num2) == expected
