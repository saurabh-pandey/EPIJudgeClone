from tests.test_base import TestBase
from tests.utils import linked_list

from search_in_list import search_list

class TestNoCycleListOverlap(TestBase):
    def test_example1(self):
        l0 = linked_list.create([1, 2, 3, 4, 5, 6, 7])
        l1 = linked_list.create([2, 3])
        from_node = search_list(l1, 3)
        to_node = search_list(l0, 4)
        from_node.next = to_node
        assert self.solve(l0, l1) is to_node
