from tests.test_base import TestBase
from tests.utils import linked_list


class TestReverseSublist(TestBase):
    def test_example1(self):
        l = linked_list.create([11, 3, 5, 7, 2])
        start = 2
        finish = 4
        l = self.solve(l, start, finish)
        expected = linked_list.create([11, 7, 5, 3, 2])
        assert l == expected
    
    def test_example2(self):
        l = linked_list.create([11, 7, 5, 3, 2])
        start = 1
        finish = 5
        l = self.solve(l, start, finish)
        expected = linked_list.create([2, 3, 5, 7, 11])
        assert l == expected
    
    def test_example3(self):
        l = linked_list.create([11, 7, 5, 3, 2])
        start = 3
        finish = 3
        l = self.solve(l, start, finish)
        expected = linked_list.create([11, 7, 5, 3, 2])
        assert l == expected
    
    def test_example4(self):
        l = linked_list.create([2])
        start = 1
        finish = 1
        l = self.solve(l, start, finish)
        expected = linked_list.create([2])
        assert l == expected
    
    def test_empty(self):
        l = linked_list.create([])
        start = 0
        finish = 0
        l = self.solve(l, start, finish)
        expected = linked_list.create([])
        assert l == expected
    
    def test_single(self):
        l = linked_list.create([1])
        start = 0
        finish = 0
        l = self.solve(l, start, finish)
        expected = linked_list.create([1])
        assert l == expected
