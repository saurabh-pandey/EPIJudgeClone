from typing import Optional

from list_node import ListNode
from test_framework import generic_test

from tests.test_even_odd_list_merge import TestEvenOddListMerge


def even_odd_merge_v1(L: ListNode) -> Optional[ListNode]:
    '''
    My O(n) time and O(1) space version
    '''
    dummy_even_head, dummy_odd_head = ListNode(0), ListNode(0)
    even, odd = dummy_even_head, dummy_odd_head
    is_odd = 0
    while L:
        if is_odd == 1:
            odd.next = L
            odd = odd.next
        else:
            even.next = L
            even = even.next
        L = L.next
        is_odd ^= 1
    odd.next = None
    even.next = dummy_odd_head.next
    return dummy_even_head.next


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    return even_odd_merge_v1(L)


if __name__ == '__main__':
    TestEvenOddListMerge(even_odd_merge_v1).run_tests()
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
