import bisect
import random

from tests.test_base import TestBase


class TestOnlineMedian(TestBase):
    def test_example1(self):
        data = [1, 0, 3, 5, 2, 0, 1]
        expected = [1, 0.5, 1, 2, 2, 1.5, 1]
        result = self.solve(iter(data))
        assert result == expected, f"Expected = {expected}, result = {result}"
    
    def test_example2(self):
        data = [4, 9, 2, 8, 2]
        expected = [4, 6.5, 4, 6.0, 4]
        result = self.solve(iter(data))
        assert result == expected, f"Expected = {expected}, result = {result}"
    
    def test_random(self):
        for size in range(1, 101):
            for _ in range(10):
                data = []
                sorted_data = []
                expected = []
                for _ in range(size):
                    value = random.randint(0, 2 * size)
                    data.append(value)
                    bisect.insort_left(sorted_data, value)
                    if len(sorted_data) % 2 == 0:
                        mid = len(sorted_data)//2
                        expected.append(
                            (sorted_data[mid - 1] + sorted_data[mid])/2)
                    else:
                        mid = len(sorted_data)//2
                        expected.append(sorted_data[mid])
                result = self.solve(iter(data))
                assert result == expected, (
                    f"data = {data}, Expected = {expected}, result = {result}")

