import random

from typing import List

from tests.test_base import TestBase


class TestKthLargestInArray(TestBase):
    def test_example1(self):
        A = [3, 2, 1, 5, 4]
        self._check_result(A)
    
    def test_random(self):
        for size in range(1, 101):
            A = [random.randint(0, 2 * size) for _ in range(size)]
            self._check_result(A)
    
    def _check_result(self, A: List[int]) -> None:
        descending_A = sorted(A, reverse=True)
        for i, expected in enumerate(descending_A):
            k = i + 1
            result = self.solve(k, A[:])
            assert result == expected, (
                f"Expected = {expected}, result = {result}, k = {k}"
            )
