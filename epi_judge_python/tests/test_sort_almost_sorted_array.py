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
    
    def test_example2(self):
        k_sorted_array = [2, 0]
        k = 1
        result = self.solve(iter(k_sorted_array), k)
        assert len(result) == len(k_sorted_array), (
                    f"Length mismatch for {k_sorted_array}, k = {k}, result = {result}")
        assert all(
            result[i] <= result[i + 1] for i in range(len(k_sorted_array) - 1)
        ), f"Result not sorted for {k_sorted_array}"
    
    def test_random(self):
        for size in range(2, 100):
            arr = [random.randint(-2 * size, 2 * size) for _ in range(size)]
            arr.sort()
            for k in range(1, size):
                k_sorted_arr = self._create_k_sorted_array(arr, k)
                result = self.solve(iter(k_sorted_arr), k)
                assert len(result) == len(k_sorted_arr), (
                    f"Length mismatch for {k_sorted_arr}, k = {k}, result = {result}")
                assert all(
                    result[i] <= result[i + 1] for i in range(
                    len(k_sorted_arr) - 1)
                ), (f"Result not sorted for {k_sorted_arr}, k = {k}, "
                   f"result = {result}")
    
    def _create_k_sorted_array(self,
                               sorted_arr: List[int],
                               k: int) -> List[int]:
        size = len(sorted_arr)
        k_sorted_arr = sorted_arr[:]
        swap_pairs = {}
        for i in range(size):
            if i not in swap_pairs:
                shift = random.randint(1, k)
                sign = 1 if i == 0 else -1 if random.randint(0, 1) == 0 else 1
                new_index = i + sign * shift
                if shift != 0 and new_index >= 0 and new_index < size:
                    if new_index not in swap_pairs:
                        swap_pairs[i] = None
                        swap_pairs[new_index] = None
        all_swap_indices = list(swap_pairs.keys())
        for i in range(0, len(all_swap_indices), 2):
            x, y = all_swap_indices[i], all_swap_indices[i + 1]
            k_sorted_arr[x], k_sorted_arr[y] = k_sorted_arr[y], k_sorted_arr[x]
        return k_sorted_arr
