import random

from tests.test_base import TestBase


class TestSortedArraysMerge(TestBase):
    def test_example1(self):
        sorted_arrays = [[3,5,7], [0, 6], [0, 6, 28]]
        result = self.solve(sorted_arrays)
        assert all(result[i] <= result[i + 1] for i in range(len(result) - 1))
    
    def test_random(self):
        for min_size in range(1, 11):
            for inc in range(21):
                max_size = min_size + inc
                for k in range(1, 20):
                    # print(f"Running for {min_size}, {max_size}, {k}")
                    sorted_arrays = self._generate_sorted_arrays(min_size, 
                                                                 max_size ,
                                                                 k)
                    result = self.solve(sorted_arrays)
                    assert all(
                        result[i] <= result[i + 1] for i in range(
                        len(result) - 1)), (
                        f"Failed for {min_size}, {max_size}, {k}")
    
    def _generate_sorted_arrays(self, min_size, max_size, k):
        sorted_arrays = []
        for _ in range(k):
            size = random.randint(min_size, max_size)
            arr = [random.randint(0, 2 * size) for _ in range(size)]
            arr.sort()
            sorted_arrays.append(arr)
        return sorted_arrays
