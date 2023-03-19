from tests.test_base import TestBase

from typing import List

class TestEvenOddArray(TestBase):
    def check_arr(self, arr: List[int]) -> bool:
        is_even_odd_split = 0
        for i in range(len(arr) - 1):
            if (arr[i] % 2 == 0) and (arr[i + 1] % 2 == 1):
                if is_even_odd_split:
                    return False
                is_even_odd_split += 1
            elif (arr[i] % 2 == 1) and (arr[i + 1] % 2 == 0):
                return False
        return True
    
    def test_example1(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        self.solve(arr)
        assert self.check_arr(arr)
    
    def test_all_odd(self):
        arr = [1, 3, 5, 7, 9, 11]
        self.solve(arr)
        assert self.check_arr(arr)
    
    def test_all_even(self):
        arr = [2, 4, 6, 8, 10, 12]
        self.solve(arr)
        assert self.check_arr(arr)
    
    def test_already_split(self):
        arr = [2, 4, 6, 8, 1, 3, 5, 7, 9]
        self.solve(arr)
        assert self.check_arr(arr)
    
    def test_complete_inverse(self):
        arr = [1, 3, 5, 7, 9, 2, 4, 6, 8]
        self.solve(arr)
        assert self.check_arr(arr)
    
    def test_initial_even(self):
        arr = [2, 4, 6, 8, 1, 3, 10, 12, 9, 2, 3, 7, 8]
        self.solve(arr)
        assert self.check_arr(arr)
    
    def test_repeated(self):
        arr = [1, 1, 2, 2, 1, 2, 1, 1, 2, 2, 1, 1, 2]
        self.solve(arr)
        assert self.check_arr(arr)
