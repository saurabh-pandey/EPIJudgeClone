from typing import Optional

from bst_node import BstNode

from test_framework import generic_test
from tests.test_search_first_greater_value_in_bst import (
    TestSearchFirstGreaterInBst)


def find_first_greater_than_k_v1(tree: BstNode, k: int) -> Optional[BstNode]:
    '''
    My version
    '''
    return None


def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    # TODO - you fill in here.
    return None


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    TestSearchFirstGreaterInBst(find_first_greater_than_k_v1).run_tests()
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
