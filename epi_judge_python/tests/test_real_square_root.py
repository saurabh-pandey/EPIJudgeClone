import math
import random

from tests.test_base import TestBase


class TestRealSquareRoot(TestBase):
    def test_example1(self):
        for _ in range(1000):
            k = random.uniform(0.0, 1000.0)
            print(f"k = {k}")
            expected = math.sqrt(k)
            result = self.solve(k)
            print(f"  expected = {expected}, result = {result}")
            assert math.isclose(expected, result), (
                f"k = {k}, expected = {expected}, result = {result}")
    
    def test_example2(self):
        for _ in range(1000):
            k = random.uniform(0.0, 1.0)
            print(f"k = {k}")
            expected = math.sqrt(k)
            result = self.solve(k)
            print(f"  expected = {expected}, result = {result}")
            assert math.isclose(expected, result), (
                f"k = {k}, expected = {expected}, result = {result}")
    
    def test_perfect_square(self):
        for i in range(100):
            sq = i * i
            print(f"x = {sq}")
            expected = math.sqrt(sq)
            result = self.solve(sq)
            print(f"  expected = {expected}, result = {result}")
            assert math.isclose(expected, result), (
                f"sq = {sq}, expected = {expected}, result = {result}")
