from typing import Optional

from list_node import ListNode
from test_framework import generic_test

from tests.test_delete_kth_last_from_list import TestDeleteKthLastFromList

def remove_kth_last_v1(L: ListNode, k: int) -> Optional[ListNode]:
    '''
    My O(n) time and O(1) space version
    '''
    length = 0
    curr = L
    while curr:
        length += 1
        curr = curr.next
    del_index = length - k
    index = 0
    prev = None
    curr = L
    while index < del_index and curr:
        prev = curr
        curr = curr.next
        index += 1
    if prev:
        prev.next = prev.next.next
        return L
    else:
        return L.next


def remove_kth_last_v2(L: ListNode, k: int) -> Optional[ListNode]:
    '''
    Book inspired O(n) time and O(1) space version
    '''
    prev = None
    iter = L
    k_ahead_iter = L
    for _ in range(k):
        k_ahead_iter = k_ahead_iter.next
    while k_ahead_iter:
        k_ahead_iter = k_ahead_iter.next
        prev = iter
        iter = iter.next
    if prev and prev.next:
        prev.next = prev.next.next
        return L
    else:
        return L.next


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    # return remove_kth_last_v1(L, k)
    return remove_kth_last_v2(L, k)


if __name__ == '__main__':
    TestDeleteKthLastFromList(remove_kth_last_v1).run_tests()
    TestDeleteKthLastFromList(remove_kth_last_v2).run_tests()
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
