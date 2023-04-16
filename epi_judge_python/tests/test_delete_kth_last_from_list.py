from tests.test_base import TestBase
from tests.utils import linked_list

from random import randint


class TestDeleteKthLastFromList(TestBase):
    def test_example1(self):
        l = linked_list.create([1, 2, 3, 4, 5, 6, 7])
        expected_l = linked_list.create([1, 2, 3, 4, 6, 7])
        l = self.solve(l, 3)
        assert l == expected_l
    
    def test_remove_last(self):
        l = linked_list.create([1, 2, 3, 4, 5, 6, 7])
        expected_l = linked_list.create([1, 2, 3, 4, 5, 6])
        l = self.solve(l, 1)
        assert l == expected_l

    def test_remove_first(self):
        l = linked_list.create([1, 2, 3, 4, 5, 6, 7])
        expected_l = linked_list.create([2, 3, 4, 5, 6, 7])
        l = self.solve(l, 7)
        assert l == expected_l
    
    def test_random(self):
        for sz in [10, 50, 100, 500, 1000] * 100:
            arr = [randint(1, 2 * sz) for _ in range(sz)]
            del_index = randint(1, sz)
            del_arr = arr[:]
            del_arr.pop(-del_index)
            l = linked_list.create(arr)
            expected_l = linked_list.create(del_arr)
            l = self.solve(l, del_index)
            assert l == expected_l, (
                f"Expected = {expected_l}, actual = {l}, sz = {sz}, index = "
                f"{del_index}")
