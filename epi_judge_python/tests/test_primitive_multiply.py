from tests.test_base import TestBase

class TestPrimitiveAddition(TestBase):
    def test_addition(self):
        for x in range(100):
            for y in range(100):
                assert self.solve(x, y) == (x + y), f"Failed for {x} + {y}"

class TestPrimitiveMultiply(TestBase):
    def test_multiplication(self):
        for x in range(100):
            for y in range(100):
                assert self.solve(x, y) == x * y, f"Failed for {x} * {y}"
