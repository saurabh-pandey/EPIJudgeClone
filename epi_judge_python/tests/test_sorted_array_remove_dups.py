from tests.test_base import TestBase

from typing import List

class TestSortedArrayRemoveDups(TestBase):
    def _checkDupsRemoved(self, A: List[int], unique_sz: int) -> bool:
        for i in range(1, unique_sz):
            if A[i] <= A[i - 1]:
                return False
        return True
    
    def test_example1(self):
        A = [2, 3, 3, 5, 7, 11, 11, 11, 13]
        expected = 6
        assert self.solve(A) == expected
        assert self._checkDupsRemoved(A, expected)
    
    def test_no_dups(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        expected = 11
        assert self.solve(A) == expected
        assert self._checkDupsRemoved(A, expected)
    
    def test_all_dups(self):
        A = [2, 2, 2, 2, 2, 2]
        expected = 1
        assert self.solve(A) == expected
        assert self._checkDupsRemoved(A, expected)
    
    def test_single(self):
        A = [3]
        expected = 1
        assert self.solve(A) == expected
        assert self._checkDupsRemoved(A, expected)
