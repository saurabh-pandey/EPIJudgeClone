from tests.test_base import TestBase
from tests.utils import linked_list


class TestEvenOddListMerge(TestBase):
    def test_example1(self):
        l = linked_list.create([0, 1, 2, 3, 4, 5])
        expected = linked_list.create([0, 2, 4, 1, 3, 5])
        actual = self.solve(l)
        assert actual == expected, (
            f"expected = {expected}, actual = {actual}"
        )
    
    def test_example2(self):
        l = linked_list.create([0, 1, 2, 3, 4, 5, 6])
        expected = linked_list.create([0, 2, 4, 6, 1, 3, 5])
        actual = self.solve(l)
        assert actual == expected, (
            f"expected = {expected}, actual = {actual}"
        )
    
    def test_all(self):
        for sz in range(1, 1000):
            arr = [i for i in range(0, sz)]
            even_arr = [e for e in range(0, sz, 2)]
            odd_arr = [o for o in range(1, sz, 2)]
            l = linked_list.create(arr)
            expected = linked_list.create(even_arr + odd_arr)
            actual = self.solve(l)
            assert actual == expected, (
                f"expected = {expected}, actual = {actual}"
            )
