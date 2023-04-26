from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from tests.test_is_tree_symmetric import TestIsTreeSymmetric


def is_symmetric_v1(tree: BinaryTreeNode) -> bool:
    '''
    My version with O(n) time and O(h) space complexity
    '''
    def check_symmetry(node0: BinaryTreeNode, node1: BinaryTreeNode) -> bool:
        if node0 and node1:
            if node0.data != node1.data:
                return False
            else:
                if (check_symmetry(node0.left, node1.right)
                    and check_symmetry(node0.right, node1.left)):
                    return True
                else:
                    return False
        elif not node0 and not node1:
            return True
        else:
            return False
    
    return not tree or check_symmetry(tree.left, tree.right)


def is_symmetric(tree: BinaryTreeNode) -> bool:
    return is_symmetric_v1(tree)


if __name__ == '__main__':
    TestIsTreeSymmetric(is_symmetric_v1).run_tests()
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
