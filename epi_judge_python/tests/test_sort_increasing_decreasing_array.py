import random

from tests.test_base import TestBase

class TestSortIncreasingDecreasingArray(TestBase):
    def test_example1(self):
        k_sorted = [1, 3, 5, 4, 2, 0, 6, 9, 12, 10, 8]
        result = self.solve(k_sorted)
        assert all(
            result[i] <= result[i + 1] for i in range(len(result) - 1)), (
            f"Failed for {k_sorted}")

    def test_random(self):
        k_sorted = []
        reverse = False
        for _ in range(1, 21):
            sz = random.randint(1, 10)
            arr = []
            for i in range(sz):
                arr.append(random.randint(0, 2 * sz))
            arr.sort(reverse=reverse)
            reverse ^= True
            k_sorted.extend(arr)
        result = self.solve(k_sorted)
        assert all(
            result[i] <= result[i + 1] for i in range(len(result) - 1)), (
            f"Failed for {k_sorted}")
