import heapq
import random

from tests.test_base import TestBase

class TestKLargestInHeap(TestBase):
    def test_example1(self):
        A = [561, 314, 401, 28, 156, 359, 271, 11, 3]
        expected = [561, 314, 401, 359]
        expected.sort()
        k = 4
        result = self.solve(A, k)
        assert expected == result, f"Expected = {expected}, result = {result}"
    
    def test_random(self):
        for size in range(1, 101):
            for _ in range(10):
                for k in range(1, size):
                    A = [-random.randint(0, 2 * size) for _ in range(size)]
                    heapq.heapify(A)
                    A = list(map(lambda x: -x, A))
                    expected = sorted(A)[:k]
                    result = self.solve(A)
                    assert expected == result, (
                        f"Expected = {expected}, result = {result}, "
                        f"A = {A}, k = {k}")
