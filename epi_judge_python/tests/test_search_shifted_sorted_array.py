import random

from tests.test_base import TestBase


class TestSearchShiftedSortedArray(TestBase):
    def test_example1(self):
        A = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
        expected = 4
        result = self.solve(A)
        assert result == expected, f"Expected = {expected}, result = {result}"
    
    def test_random(self):
        for size in range(11):
            shift_right_by = random.randint(0, size - 1)
            unique_nums = set()
            while len(unique_nums) < shift_right_by:
                unique_nums.add(random.randint(2 * size, 5 * size))
            first_part = sorted(unique_nums)
            unique_nums.clear()
            while len(unique_nums) < size - shift_right_by:
                unique_nums.add(random.randint(0, 2 * size - 1))
            second_part = sorted(unique_nums)
            A = first_part + second_part
            result = self.solve(A)
            assert result == shift_right_by, (
                f"Expected = {shift_right_by}, result = {result}")
