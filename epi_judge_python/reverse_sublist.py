from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from tests.test_reverse_sublist import TestReverseSublist


def reverse_sublist_v1(L: ListNode,
                       start: int,
                       finish: int) -> Optional[ListNode]:
    '''
    My version
    '''
    pass

def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    # TODO - you fill in here.
    return None


if __name__ == '__main__':
    TestReverseSublist(reverse_sublist_v1).run_tests()
    # exit(
    #     generic_test.generic_test_main('reverse_sublist.py',
    #                                    'reverse_sublist.tsv', reverse_sublist))
