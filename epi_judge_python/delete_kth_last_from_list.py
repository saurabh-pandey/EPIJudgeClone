from typing import Optional

from list_node import ListNode
from test_framework import generic_test

from tests.test_delete_kth_last_from_list import TestDeleteKthLastFromList

def remove_kth_last_v1(L: ListNode, k: int) -> Optional[ListNode]:
    '''
    My attempt
    '''
    pass

# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    # TODO - you fill in here.
    return None


if __name__ == '__main__':
    TestDeleteKthLastFromList(remove_kth_last_v1).run_tests()
    # exit(
    #     generic_test.generic_test_main('delete_kth_last_from_list.py',
    #                                    'delete_kth_last_from_list.tsv',
    #                                    remove_kth_last))
