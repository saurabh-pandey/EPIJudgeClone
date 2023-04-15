from tests.test_base import TestBase
from tests.utils import linked_list

from random import randint

class TestDeleteKthLastFromList(TestBase):
    def test_example1(self):
        l = linked_list.create([1, 2, 3, 4, 5, 6, 7])
        expected_l = linked_list.create([1, 2, 3, 4, 6, 7])
        del_node = self.solve(l, 3)
        assert l == expected_l
        assert del_node.data == 5
    
    def test_random(self):
        for sz in [10, 50, 100, 500, 1000] * 5:
            arr = [randint(1, 2 * sz) for _ in range(sz)]
            del_index = randint(0, sz - 1)
            del_arr = arr[:]
            del_arr.pop(-del_index)
            l = linked_list.create(arr)
            expected_l = linked_list.create(del_arr)
            del_node = self.solve(l, del_index)
            assert l == expected_l
            assert del_node.data == arr[-del_index]
