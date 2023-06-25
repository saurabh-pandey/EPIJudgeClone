from typing import Optional

from list_node import ListNode

from test_framework import generic_test

from tests.test_sort_list import TestSortList


def stable_sort_list_v1(L: ListNode) -> Optional[ListNode]:
    '''
    O(n^2) bubble sort of a linked list
    '''
    is_swapped = True
    head = ListNode(-1, L)
    while is_swapped:
        is_swapped = False
        prev = head
        node = head.next
        while node:
            if node.next and node.data > node.next.data:
                prev.next = node.next
                node.next = node.next.next
                prev.next.next = node
                is_swapped = True
            prev = node
            node = node.next
    return head.next


def stable_sort_list(L: ListNode) -> Optional[ListNode]:
    return stable_sort_list_v1(L)


if __name__ == '__main__':
    TestSortList(stable_sort_list_v1).run_tests()
    exit(
        generic_test.generic_test_main('sort_list.py', 'sort_list.tsv',
                                       stable_sort_list))
