import random

from typing import List

from tests.test_base import TestBase


class TestSortAlmostSortedArray(TestBase):
    def test_example1(self):
        k_sorted_array = [3, -1, 2, 6, 4, 5, 8]
        k = 2
        result = self.solve(iter(k_sorted_array), k)
        assert len(result) == len(k_sorted_array), f"Length mismatch"
        assert all(
            result[i] <= result[i + 1] for i in range(len(k_sorted_array) - 1)
        ), f"Result not sorted for {k_sorted_array}"
    
    def test_random(self):
        for size in range(1, 100):
            arr = [random.randint(-2 * size, 2 * size) for _ in range(size)]
            arr.sort()
            for _ in range(10):
                k = random.randint(1, size - 1)
                k_sorted_arr = self._create_k_sorted_array(arr, k)
                result = self.solve(iter(k_sorted_arr), k)
                assert len(result) == len(k_sorted_arr), f"Length mismatch"
                assert all(
                    result[i] <= result[i + 1] for i in range(
                    len(k_sorted_arr) - 1)
                ), f"Result not sorted for {k_sorted_arr}"
    
    def _create_k_sorted_array(sorted_arr: List[int], k: int) -> List[int]:
        size = len(sorted_arr)
        k_sorted_arr = [-1 for _ in sorted_arr]
        index_map = {}
        for i in range(size):
            min_index = 0 if i - k < 0 else i - k
            max_index = size - 1 if i + k >= size else i + k
            possible_indices = []
            for index in range(min_index, max_index + 1):
                if index not in index_map:
                    possible_indices.append(index)
            new_index = possible_indices[random.randint(
                0, len(possible_indices) - 1)]
            index_map[new_index] = i
        for dest, orig in index_map.keys():
            k_sorted_arr[dest] = sorted_arr[orig]
        return k_sorted_arr
