import random

from tests.test_base import TestBase

from tests.utils import linked_list

from list_node import ListNode

class TestSortList(TestBase):
    def test_example1(self):
        l_list: ListNode = linked_list.create([3, 5, 0, 4, 2, 1])
        result: ListNode = self.solve(l_list)
        assert self._check_sorted(result), (
            f"Sorting failed for {l_list} with result = {result}")
    
    def test_stability(self):
        l_list: ListNode = linked_list.create([3, 5, 0, 4, 0, 2, 1, 3, 1])
        node_ids_order = {0: [], 3: []}
        node = l_list
        while node:
            if node.data in node_ids_order:
                node_ids_order[node.data].append(node)
            node = node.next
        result: ListNode = self.solve(l_list)
        assert self._check_sorted(result), (
            f"Sorting failed for {l_list} with result = {result}")
        for nodes in node_ids_order.values():
            node = nodes[0]
            for n in nodes[1:]:
                assert node.next == n, f"Not stable at {n.data}"
                node = node.next
    
    def test_random(self):
        for sz in range(1, 100):
            for _ in range(10):
                random_list = [random.randint(0, sz) for _ in range(sz)]
                l_list: ListNode = linked_list.create(random_list)
                result: ListNode = self.solve(l_list)
                assert self._check_sorted(result), (
                    f"Sorting failed for {l_list} with result = {result}")
    
    def _check_sorted(self, head: ListNode):
        node: ListNode = head
        while node and node.next:
            if node.data > node.next.data:
                return False
            node = node.next
        return True
