from tests.test_base import TestBase
from tests.utils import int_as_array

class TestIntAsArrayAdd(TestBase):
    def test_example1(self):
        for i in range(1000):
            num1 = int_as_array.convert(i)
            for j in range(1000):
                num2 = int_as_array.convert(j)
                expected = int_as_array.convert(i + j)
                assert self.solve(num1, num2) == expected

class TestIntAsArrayMultiply(TestBase):
    def test_example1(self):
        for i in range(-250, 251):
            num1 = int_as_array.convert(i)
            for j in range(-250, 251):
                num2 = int_as_array.convert(j)
                expected = int_as_array.convert(i * j)
                assert self.solve(num1, num2) == expected
