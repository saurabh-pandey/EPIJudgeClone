from tests.test_base import TestBase
from tests.utils import linked_list

from random import randint


class TestSortedListsMerge(TestBase):
    def test_example1(self):
        l1 = linked_list.create([2, 5, 7])
        l2 = linked_list.create([3, 11])
        merged_l = self.solve(l1, l2)
        expected = linked_list.create([2, 3, 5, 7, 11])
        assert merged_l == expected
    
    def test_one_less(self):
        l1 = linked_list.create([1, 2, 3])
        l2 = linked_list.create([4, 5, 6])
        merged_l = self.solve(l1, l2)
        expected = linked_list.create([1, 2, 3, 4, 5, 6])
        assert merged_l == expected
    
    def test_one_greater(self):
        l1 = linked_list.create([4, 5, 6])
        l2 = linked_list.create([1, 2, 3])
        merged_l = self.solve(l1, l2)
        expected = linked_list.create([1, 2, 3, 4, 5, 6])
        assert merged_l == expected
    
    def test_one_empty(self):
        l1 = linked_list.create([])
        l2 = linked_list.create([1, 2, 3])
        merged_l = self.solve(l1, l2)
        expected = linked_list.create([1, 2, 3])
        assert merged_l == expected
    
    def test_other_empty(self):
        l1 = linked_list.create([1, 2, 3])
        l2 = linked_list.create([])
        merged_l = self.solve(l1, l2)
        expected = linked_list.create([1, 2, 3])
        assert merged_l == expected
    
    def test_all_constant(self):
        l1 = linked_list.create([1, 1, 1])
        l2 = linked_list.create([1, 1])
        merged_l = self.solve(l1, l2)
        expected = linked_list.create([1, 1, 1, 1, 1])
        assert merged_l == expected
    
    def test_pairwise_constant(self):
        l1 = linked_list.create([1, 1, 1])
        l2 = linked_list.create([2, 2])
        merged_l = self.solve(l1, l2)
        expected = linked_list.create([1, 1, 1, 2, 2])
        assert merged_l == expected
    
    def test_random(self):
        for size1 in [5, 10, 50, 100, 500, 1000]:
            arr1 = [randint(1, 2 * size1) for _ in range(size1)]
            arr1.sort()
            for size2 in [5, 10, 50, 100, 500, 1000]:
                l1 = linked_list.create(arr1)
                arr2 = [randint(1, 2 * size2) for _ in range(size2)]
                arr2.sort()
                result_arr = arr1 + arr2
                result_arr.sort()
                l2 = linked_list.create(arr2)
                merged_l = self.solve(l1, l2)
                expected = linked_list.create(result_arr)
                assert merged_l == expected
