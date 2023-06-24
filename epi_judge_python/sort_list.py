from typing import Optional

from list_node import ListNode

from test_framework import generic_test

from tests.test_sort_list import TestSortList


def stable_sort_list_v1(L: ListNode) -> Optional[ListNode]:
    pass

def stable_sort_list(L: ListNode) -> Optional[ListNode]:
    # TODO - you fill in here.
    return None


if __name__ == '__main__':
    TestSortList(stable_sort_list_v1).run_tests()
    # exit(
    #     generic_test.generic_test_main('sort_list.py', 'sort_list.tsv',
    #                                    stable_sort_list))
