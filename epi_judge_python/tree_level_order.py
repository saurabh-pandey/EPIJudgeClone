from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from tests.test_tree_level_order import TestTreeLevelOrder


def binary_tree_depth_order_v1(tree: BinaryTreeNode) -> List[List[int]]:
    '''
    My version
    '''
    if not tree:
        return []
    result = []
    nodes_queue = [tree]
    while nodes_queue:
        result.append([node.data for node in nodes_queue])
        next_nodes = []
        for node in nodes_queue:
            if node.left:
                next_nodes.append(node.left)
            if node.right:
                next_nodes.append(node.right)
        nodes_queue = next_nodes
    return result

def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    return binary_tree_depth_order_v1(tree)


if __name__ == '__main__':
    TestTreeLevelOrder(binary_tree_depth_order_v1).run_tests()
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
