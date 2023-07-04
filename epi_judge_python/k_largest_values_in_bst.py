from typing import List, Optional

from bst_node import BstNode

from test_framework import generic_test, test_utils
from tests.test_k_largest_values_in_bst import TestKLargestInBst


def find_k_largest_in_bst_v1(tree: BstNode, k: int) -> List[int]:
    '''
    My version with O(k + h) time where k is number of values and h is the max
    height. O(h) is space.
    '''
    def reverse_inorder(node: Optional[BstNode], 
                        k: int,
                        result: List[int]) -> bool:
        if node is None:
            return False
        do_stop = reverse_inorder(node.right, k, result)
        if do_stop:
            return True
        result.append(node.data)
        if len(result) == k:
            return True
        return reverse_inorder(node.left, k, result)
    result = []
    reverse_inorder(tree, k, result)
    return result


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    return find_k_largest_in_bst_v1(tree, k)


if __name__ == '__main__':
    TestKLargestInBst(find_k_largest_in_bst_v1).run_tests()
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
