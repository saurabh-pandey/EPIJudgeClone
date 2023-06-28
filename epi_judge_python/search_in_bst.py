from typing import Optional

from bst_node import BstNode
from test_framework import generic_test

from tests.test_search_in_bst import TestSearchInBst


def search_bst_v1(tree: BstNode, key: int) -> Optional[BstNode]:
    '''
    My O(h) version with h being the max height of the tree
    '''
    if tree is None:
        return None
    elif key == tree.data:
        return tree
    elif key < tree.data:
        return search_bst_v1(tree.left, key)
    else:
        return search_bst_v1(tree.right, key)


def search_bst(tree: BstNode, key: int) -> Optional[BstNode]:
    return search_bst_v1(tree, key)


def search_bst_wrapper(tree, key):
    result = search_bst(tree, key)
    return result.data if result else -1


if __name__ == '__main__':
    TestSearchInBst(search_bst_v1).run_tests()
    exit(
        generic_test.generic_test_main('search_in_bst.py', 'search_in_bst.tsv',
                                       search_bst_wrapper))
