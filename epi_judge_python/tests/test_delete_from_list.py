from tests.test_base import TestBase
from tests.utils import linked_list

from list_node import ListNode
from search_in_list import search_list

class TestDeleteFromList(TestBase):
    def test_example1(self):
        ll = linked_list.create([1, 2, 2, 3])
        node = search_list(ll, 2)
        self.solve(node)
        expected = linked_list.create([1, 2, 3])
        assert ll == expected