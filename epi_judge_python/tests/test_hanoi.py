from typing import List

from tests.test_base import TestBase

class TestHanoi(TestBase):
    def steps_count(num_rings: int) -> int:
        num_steps = 0
        for _ in range(num_rings):
            num_steps = 2 * num_steps + 1
        return num_steps
    
    def test_all(self):
        for num_rings in range(10):
            result: List[List[int]] = self.solve(num_rings)
            expected_size = TestHanoi.steps_count(num_rings)
            assert len(result) == expected_size, (
                f"Incorrect size expected {expected_size} != {len(result)}")
