from typing import Optional, Tuple

from tests.test_base import TestBase
from tests.utils import linked_list

from list_node import ListNode
from search_in_list import search_list


class TestIsListCyclic(TestBase):
    def _create_cyclic_list(
            self,
            start: int,
            finish: int,
            cycle: Optional[int] = None) -> Tuple[ListNode, ListNode]:
        ll = linked_list.create([i for i in range(start, finish + 1)])
        if not cycle:
            return ll, None
        cycle_start_node = search_list(ll, cycle)
        cycle_end_node = search_list(ll, finish)
        cycle_end_node.next = cycle_start_node
        return ll, cycle_start_node
    
    def test_example1(self):
        head, cycle_start_node = self._create_cyclic_list(1, 8, 3)
        cycle_node = self.solve(head)
        assert cycle_node is cycle_start_node
    
    def test_no_cycle(self):
        head, cycle_start_node = self._create_cyclic_list(1, 8)
        cycle_node = self.solve(head)
        assert cycle_node is cycle_start_node
    
    def test_full_cycle(self):
        head, cycle_start_node = self._create_cyclic_list(1, 8, 1)
        cycle_node = self.solve(head)
        assert cycle_node is cycle_start_node
    
    def test_single(self):
        head, cycle_start_node = self._create_cyclic_list(1, 1)
        cycle_node = self.solve(head)
        assert cycle_node is cycle_start_node
