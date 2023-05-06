from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test

from tests.test_tree_with_parent_inorder import TestTreeWithParentInorder


def inorder_traversal_v1(tree: BinaryTreeNode) -> List[int]:
    pass

def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    # TODO - you fill in here.
    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
