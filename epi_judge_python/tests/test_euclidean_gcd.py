import math

from tests.test_base import TestBase


class TestEuclideanGcd(TestBase):
    def test_all(self):
        for i in range(1, 100):
            for j in range(1, i):
                result = self.solve(i, j)
                expected = math.gcd(i, j)
                assert result == expected, f"{expected} != {result} result"
    
    def test_zero(self):
        x = 42
        y = 0
        result = self.solve(x, y)
        expected = math.gcd(x, y)
        assert result == expected, f"{expected} != {result} result"
