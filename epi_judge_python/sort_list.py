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


def merge_two_sorted_lists(L0: Optional[ListNode],
                           L1: Optional[ListNode]) -> Optional[ListNode]:
    dummy_head: ListNode = ListNode(None, None)
    tail = dummy_head
    while L0 and L1:
        if L0.data <= L1.data:
            tail.next = L0
            L0 = L0.next
        else:
            tail.next = L1
            L1 = L1.next
        tail = tail.next
    tail.next = L0 or L1
    return dummy_head.next


def stable_sort_list_v3(L: ListNode) -> Optional[ListNode]:
    '''
    O(n*log(n)) time and O(log(n)) space merge sort of a linked list
    '''
    if L is None or L.next is None:
        return L
    pre_slow, slow, fast = None, L, L
    while fast and fast.next:
        pre_slow = slow
        slow, fast = slow.next, fast.next.next
    if pre_slow:
        pre_slow.next = None
    
    return merge_two_sorted_lists(stable_sort_list_v3(L),
                                  stable_sort_list_v3(slow))


def stable_sort_list(L: ListNode) -> Optional[ListNode]:
    # return stable_sort_list_v1(L)
    # return stable_sort_list_v2(L)
    return stable_sort_list_v3(L)


if __name__ == '__main__':
    TestSortList(stable_sort_list_v1).run_tests()
    TestSortList(stable_sort_list_v2).run_tests()
    TestSortList(stable_sort_list_v3).run_tests()
    exit(
        generic_test.generic_test_main('sort_list.py', 'sort_list.tsv',
                                       stable_sort_list))
