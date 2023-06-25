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
