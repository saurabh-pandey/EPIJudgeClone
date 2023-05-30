import random

from typing import List

from tests.test_base import TestBase


class TestSearchMissingElement(TestBase):
    def test_all(self):
        for size in range(2, 1000):
            orig_arr = [i for i in range(size)]
            for _ in range(10):
                A = orig_arr[:]
                index = random.randint(0, size - 1)
                if index > 0 and index < size - 1:
                    self._check_smaller(index, A)
                    self._check_larger(index, A)
                elif index == 0:
                    self._check_larger(index, A)
                else:
                    self._check_smaller(index, A)
    
    def _check_smaller(self, index: int, A: List[int]) -> None:
        new_smaller_val = random.randint(0, index - 1)
        A[index] = new_smaller_val
        duplicate, missing = self.solve(A)
        assert duplicate == new_smaller_val, (
            f"Expected duplicate = {new_smaller_val},"
            f" found = {duplicate}, A = {A}")
        assert missing == index, (
            f"Expected missing = {index},"
            f" found = {missing}, A = {A}")
    
    def _check_larger(self, index: int, A: List[int]) -> None:
        new_larger_val = random.randint(index + 1, len(A) - 1)
        A[index] = new_larger_val
        duplicate, missing = self.solve(A)
        assert duplicate == new_larger_val, (
            f"Expected duplicate = {new_larger_val},"
            f" found = {duplicate}, A = {A}")
        assert missing == index, (
            f"Expected missing = {index},"
            f" found = {missing}, A = {A}")
