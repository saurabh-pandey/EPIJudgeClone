from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from tests.test_is_tree_balanced import TestIsTreeBalanced

from typing import Tuple, Optional

def is_balanced_binary_tree_v1(tree: BinaryTreeNode) -> bool:
    '''
    My O(n) time and O(h) space version
    '''
    def evaluate_height(node: BinaryTreeNode) -> Tuple[bool, Optional[int]]:
        if node is None:
            return (True, 0)
        is_left_bal, left_ht = evaluate_height(node.left)
        if is_left_bal == False:
            return (False, None)
        is_right_bal, right_ht = evaluate_height(node.right)
        if is_right_bal == False:
            return (False, None)
        if abs(left_ht - right_ht) > 1:
            return (False, None)
        return (True, max(left_ht, right_ht) + 1)
    
    is_balanced, _ = evaluate_height(tree)
    return is_balanced


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    return is_balanced_binary_tree_v1(tree)


if __name__ == '__main__':
    TestIsTreeBalanced(is_balanced_binary_tree_v1).run_tests()
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
