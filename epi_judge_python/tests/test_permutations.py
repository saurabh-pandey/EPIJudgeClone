import itertools

from typing import List

from tests.test_base import TestBase


class TestPermutations(TestBase):
    def test_example1(self):
        A = [1, 2, 3]
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2],
                    [3, 2, 1]]
        result = self.solve(A)
        result.sort()
        assert expected == result, f"Expected {expected} != {result} result"
    
    def test_all(self):
        for n in range(1, 10):
            A = list(range(n))
            result = self.solve(A)
            self.check_permutations(A, result)
    
    def check_permutations(self, A: List[int], result: List[List[int]]):
        expected: List[List[int]] = [list(p) for p in itertools.permutations(A)]
        result.sort()
        assert expected == result, f"Expected {expected} != {result} result"
