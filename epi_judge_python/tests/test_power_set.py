from itertools import chain, combinations
from typing import List

from tests.test_base import TestBase

def powerset(input_set: List[int]) -> List[List[int]]:
    power_set = []
    for subset in chain.from_iterable(
            combinations(input_set, r) for r in range(len(input_set) + 1)):
        power_set.append(list(subset))
    return power_set

class TestPowerSet(TestBase):
    def test_all(self):
        for sz in range(6):
            input_set = list(range(sz))
            expected = powerset(input_set)
            result: List[List[int]] = self.solve(input_set)
            expected.sort()
            result.sort()
            assert result == expected, f"Expected {expected} != {result}"
