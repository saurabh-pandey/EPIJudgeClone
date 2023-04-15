import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from tests.test_do_terminated_lists_overlap import TestNoCycleListOverlap


def overlapping_no_cycle_lists_v1(l0: ListNode, l1: ListNode) -> ListNode:
    '''
    My O(n) time and O(1) space version
    '''
    def length(l: ListNode) -> int:
        sz = 0
        while l:
            sz += 1
            l = l.next
        return sz
    l0_sz, l1_sz = length(l0), length(l1)
    if l1_sz > l0_sz:
        l0, l1 = l1, l0 # l1 is bigger so l0 points to it in this case
    # Invariant from here is the l0 is always the bigger list
    diff_sz = abs(l0_sz - l1_sz)
    for _ in range(diff_sz):
        l0 = l0.next
    while l0 and l1 and l0 is not l1:
        l0, l1 = l0.next, l1.next
    return l0


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    return overlapping_no_cycle_lists_v1(l0, l1)


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    TestNoCycleListOverlap(overlapping_no_cycle_lists_v1).run_tests()
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
