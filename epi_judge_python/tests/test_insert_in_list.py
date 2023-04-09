from tests.test_base import TestBase

from tests.utils import linked_list

from list_node import ListNode

from search_in_list import search_list


class TestInsertInList(TestBase):
    def test_example1(self):
        l = linked_list.create([1, 2, 3])
        node = search_list(l, 3)
        self.solve(node, ListNode(4))
        expected = linked_list.create([1, 2, 3, 4])
        assert l == expected
    
    def test_example2(self):
        l = linked_list.create([1, 3, 4])
        node = search_list(l, 1)
        self.solve(node, ListNode(2))
        expected = linked_list.create([1, 2, 3, 4])
        assert l == expected
    
    def test_example3(self):
        l = linked_list.create([1, 2, 4])
        node = search_list(l, 2)
        self.solve(node, ListNode(3))
        expected = linked_list.create([1, 2, 3, 4])
        assert l == expected
