from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from tests.test_sorted_lists_merge import TestSortedListsMerge


def merge_two_sorted_lists_v1(L1: Optional[ListNode],
                              L2: Optional[ListNode]) -> Optional[ListNode]:
    '''
    My O(n + m) space and time complexity version
    '''
    def assign_node(head: Optional[ListNode],
                    current: Optional[ListNode],
                    data: int) -> None:
        if not head:
            head = ListNode(data)
            current = head
        else:
            current.next = ListNode(data)
            current = current.next
        return head, current
    iter_l1 = L1
    iter_l2 = L2
    head = None
    curr_node = None
    while iter_l1 and iter_l2:
        data = None
        if iter_l1.data <= iter_l2.data:
            data = iter_l1.data
            iter_l1 = iter_l1.next
        else:
            data = iter_l2.data
            iter_l2 = iter_l2.next
        head, curr_node = assign_node(head, curr_node, data)
    while iter_l1:
        head, curr_node = assign_node(head, curr_node, iter_l1.data)
        iter_l1 = iter_l1.next
    while iter_l2:
        head, curr_node = assign_node(head, curr_node, iter_l2.data)
        iter_l2 = iter_l2.next
    return head

def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    return merge_two_sorted_lists_v1(L1, L2)


if __name__ == '__main__':
    TestSortedListsMerge(merge_two_sorted_lists_v1).run_tests()
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
