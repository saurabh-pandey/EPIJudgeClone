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
            pow_set = powerset(input_set)
            print(f"{input_set} => {pow_set}")
