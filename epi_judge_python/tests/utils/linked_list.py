from typing import List

from list_node import ListNode

def create(lst: List[int]) -> ListNode:
    head = None
    for l in reversed(lst):
        head = ListNode(l, head)
    return head
