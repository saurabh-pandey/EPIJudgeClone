from typing import Optional

from list_node import ListNode

from test_framework import generic_test

from tests.test_sort_list import TestSortList


def stable_sort_list_v1(L: ListNode) -> Optional[ListNode]:
    '''
    O(n^2) bubble sort of a linked list
    '''
    is_swapped = True
    dummy_head = ListNode(None, L)
    while is_swapped:
        is_swapped = False
        prev = dummy_head
        node = dummy_head.next
        while node:
            if node.next and node.data > node.next.data:
                prev.next = node.next
                node.next = node.next.next
                prev.next.next = node
                is_swapped = True
            prev = node
            node = node.next
    return dummy_head.next


def stable_sort_list_v2(L: ListNode) -> Optional[ListNode]:
    '''
    O(n^2) insertion sort of a linked list
    '''
    dummy_head: ListNode = ListNode(None, L)
    start_node: ListNode = dummy_head
    while start_node and start_node.next:
        prev: ListNode = start_node
        node: ListNode = start_node.next
        min_node: ListNode = node
        min_node_prev: ListNode = prev
        while node:
            if node.data < min_node.data:
                min_node = node
                min_node_prev = prev
            prev = node
            node = node.next
        min_node_prev.next = min_node.next
        min_node.next = start_node.next
        start_node.next = min_node
        start_node = start_node.next
    return dummy_head.next


def stable_sort_list(L: ListNode) -> Optional[ListNode]:
    # return stable_sort_list_v1(L)
    return stable_sort_list_v2(L)


if __name__ == '__main__':
    TestSortList(stable_sort_list_v1).run_tests()
    TestSortList(stable_sort_list_v2).run_tests()
    exit(
        generic_test.generic_test_main('sort_list.py', 'sort_list.tsv',
                                       stable_sort_list))
