from tests.test_base import TestBase

from tests.utils import linked_list


class TestSearchInList(TestBase):
    def test_example1(self):
        l = linked_list.create([1, 2, 3])
        node = self.solve(l, 2)
        assert node.data == 2
    
    def test_example2(self):
        l = linked_list.create([1, 2, 3])
        node = self.solve(l, 1)
        assert node.data == 1
    
    def test_example3(self):
        l = linked_list.create([1, 2, 3])
        node = self.solve(l, 3)
        assert node.data == 3
    
    def test_example4(self):
        l = linked_list.create([1, 2, 3])
        node = self.solve(l, 4)
        assert node == None
    
    def test_example5(self):
        l = linked_list.create([])
        node = self.solve(l, 4)
        assert node == None
    
    def test_example6(self):
        l = linked_list.create([1])
        node = self.solve(l, 1)
        assert node.data == 1
    
    def test_example7(self):
        l = linked_list.create([1])
        node = self.solve(l, 2)
        assert node == None
