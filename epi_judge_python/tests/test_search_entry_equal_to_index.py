import random

from typing import List

from tests.test_base import TestBase


class TestSearchEntryEqualToIndex(TestBase):
    def test_example1(self):
        A = [-2, 0, 2, 3, 6, 7, 9]
        result = self.solve(A)
        assert self._check(A, result), (
            f"Failed for A = {A} with result = {result}")
    
    def test_random(self):
        for size1 in range(21):
            unique_nums = set()
            while len(unique_nums) < size1:
                unique_nums.add(random.randint(-2 * size1, size1 - 1))
            first_part = sorted(unique_nums)
            for size2 in range(21):
                unique_nums.clear()
                while len(unique_nums) < size2:
                    unique_nums.add(
                        random.randint(size1 + size2 + 1, 5 * (size1 + size2)))
                second_part = sorted(unique_nums)
                A = first_part + [size1] + second_part
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
