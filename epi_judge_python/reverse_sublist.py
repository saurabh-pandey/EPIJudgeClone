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
        if not node.next or depth == 1:
            return node, node
        new_head, _ = reverse(node.next, depth - 1)
        node.next.next = node
        return new_head, node
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
    # TODO - you fill in here.
    return reverse_sublist_v1(L, start, finish)


if __name__ == '__main__':
    TestReverseSublist(reverse_sublist_v1).run_tests()
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
