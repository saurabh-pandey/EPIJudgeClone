from tests.test_base import TestBase

class TestStringToIntegerConversion(TestBase):
    def test_example1(self):
        for n in range(-1000, 1001):
            assert self.solve(str(n)) == n

class TestIntegerToStringConversion(TestBase):
    def test_example1(self):
        for n in range(-1000, 1001):
            assert self.solve(n) == str(n)
