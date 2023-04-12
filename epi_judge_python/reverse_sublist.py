from typing import Optional, Tuple

from list_node import ListNode
from test_framework import generic_test
from tests.test_reverse_sublist import TestReverseSublist


def reverse_sublist_v1(L: ListNode,
                       start: int,
                       finish: int) -> Optional[ListNode]:
    '''
    My version with O(n) time and space
    '''
    def reverse(node: ListNode, depth: int) -> Tuple[ListNode, ListNode]:
        node_stack = []
        for _ in range(depth):
            node_stack.append(node)
            node = node.next
        curr_node = node_stack.pop()
        new_head, new_tail = curr_node, curr_node
        while node_stack:
            curr_node = node_stack.pop()
            curr_node.next.next = curr_node
            new_tail = curr_node
        return new_head, new_tail
    if not L:
        return L
    if start == finish:
        return L
    count = 1
    prev_to_start = None
    start_node = L
    while count < start:
        count += 1
        prev_to_start = start_node
        start_node = start_node.next
    finish_node = start_node
    while count <= finish:
        count += 1
        finish_node = finish_node.next
    rev_head, rev_tail = reverse(start_node, finish - start + 1)
    rev_tail.next = finish_node
    if prev_to_start:
        prev_to_start.next = rev_head
        return L
    else:
        return rev_head


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    return reverse_sublist_v1(L, start, finish)


if __name__ == '__main__':
    TestReverseSublist(reverse_sublist_v1).run_tests()
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
