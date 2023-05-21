import random

from typing import List

from tests.test_base import TestBase


class TestSearchEntryEqualToIndex(TestBase):
    def test_example1(self):
        A = [-2, 0, 2, 3, 6, 7, 9]
        result = self.solve(A)
        assert self._check(A, result), (
            f"Failed for A = {A} with result = {result}")        

    def _check(self, A: List[int], result: int) -> bool:
        if result != -1:
            if A[result] != result:
                return False
        else:
            if any(i == A[i] for i in range(len(A))):
                return False
        return True
