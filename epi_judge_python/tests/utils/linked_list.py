from typing import List

from list_node import ListNode

def create(lst: List[int]) -> ListNode:
    '''
    Create singly linked list from a list
    '''
    head = None
    for l in reversed(lst):
        head = ListNode(l, head)
    return head
