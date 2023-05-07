from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test

from tests.test_tree_with_parent_inorder import TestTreeWithParentInorder


def inorder_traversal_v1(tree: BinaryTreeNode) -> List[int]:
    '''
    Constant space and O(n) time version
    '''
    node = tree
    prev = None
    inorder = []
    while node:
        if prev and (prev is node.right):
            prev = node
            node = node.parent
        elif prev is node.parent and node.left:
            prev = node
            node = node.left
        else:
            inorder.append(node.data)
            prev = node
            if node.right:
                node = node.right
            else:
                node = node.parent
    return inorder


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    return inorder_traversal_v1(tree)


if __name__ == '__main__':
    TestTreeWithParentInorder(inorder_traversal_v1).run_tests()
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
