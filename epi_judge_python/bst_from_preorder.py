from typing import List, Optional

from bst_node import BstNode

from test_framework import generic_test

from tests.test_bst_from_preorder import TestBstFromPreorder


def rebuild_bst_from_preorder_v1(
        preorder_sequence: List[int]) -> Optional[BstNode]:
    return None


def rebuild_bst_from_preorder(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:
    # TODO - you fill in here.
    return None


if __name__ == '__main__':
    TestBstFromPreorder(rebuild_bst_from_preorder_v1).run_tests()
    # exit(
    #     generic_test.generic_test_main('bst_from_preorder.py',
    #                                    'bst_from_preorder.tsv',
    #                                    rebuild_bst_from_preorder))
