from typing import Optional

from bst_node import BstNode

from test_framework import generic_test
from tests.test_search_first_greater_value_in_bst import (
    TestSearchFirstGreaterInBst)


def find_first_greater_than_k_v1(tree: BstNode, k: int) -> Optional[BstNode]:
    '''
    My version with O(h) where h is the max tree height and O(1) space
    '''
    last_found_greater: Optional[BstNode] = None
    node = tree
    while node:
        if k < node.data:
            last_found_greater = node
            node = node.left
        else:
            node = node.right
    return last_found_greater


def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    return find_first_greater_than_k_v1(tree, k)


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
