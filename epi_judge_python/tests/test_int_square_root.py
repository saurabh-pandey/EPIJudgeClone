import math

from tests.test_base import TestBase


class TestIntSquareRoot(TestBase):
    def test_int_sqrt(self):
        for N in range(0, 100000):
            expected = math.floor(math.sqrt(N))
            result = self.solve(N)
            assert result == expected, (
                f"Expected = {expected}, result = {result}, N = {N}")
