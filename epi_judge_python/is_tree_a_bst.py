from binary_tree_node import BinaryTreeNode

from test_framework import generic_test
from tests.test_is_tree_a_bst import TestIsTreeBst


def is_binary_tree_bst_v1(tree: BinaryTreeNode) -> bool:
    pass


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    return True


if __name__ == '__main__':
    TestIsTreeBst(is_binary_tree_bst_v1).run_tests()
    # exit(
    #     generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
    #                                    is_binary_tree_bst))
