import functools

from collections import namedtuple
from typing import List, Optional, Dict

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from tests.test_lowest_common_ancestor import TestLowestCommonAncestor


def lca_v1(tree: BinaryTreeNode,
           node0: BinaryTreeNode,
           node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    '''
    My version of LCA with O(n) time and O(h) space bounds
    '''
    def search_lca(node: BinaryTreeNode,
                   node0: BinaryTreeNode,
                   node1: BinaryTreeNode,
                   path: List[BinaryTreeNode],
                   ancestry: Dict[int, List[BinaryTreeNode]]) -> Optional[BinaryTreeNode]:
        if node is None:
            return None
        path.append(node)
        if node is node0:
            ancestry[0] = path[:]
        if node is node1:
            ancestry[1] = path[:]
        if all([i in ancestry for i in [0, 1]]):
            last_match = ancestry[0][0]
            for i in range(1, min(len(ancestry[0]), len(ancestry[1]))):
                if ancestry[0][i] is ancestry[1][i]:
                    last_match = ancestry[0][i]
                else:
                    break
            return last_match
        lca_node = search_lca(node.left, node0, node1, path, ancestry)
        if lca_node:
            return lca_node
        lca_node = search_lca(node.right, node0, node1, path, ancestry)
        if lca_node:
            return lca_node
        path.pop()
        return None
    path = []
    ancestry = {}
    return search_lca(tree, node0, node1, path, ancestry)


def lca_v2(tree: BinaryTreeNode,
           node0: BinaryTreeNode,
           node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    '''
    Book's version with same time and space bounds
    '''
    Status = namedtuple("Status", ("num_target_nodes", "ancestor"))

    def lca_helper(node: BinaryTreeNode,
                   node0: BinaryTreeNode,
                   node1: BinaryTreeNode) -> Status:
        if not node:
            return Status(0, None)
        left_status = lca_helper(node.left, node0, node1)
        if left_status.num_target_nodes == 2:
            return left_status
        right_status = lca_helper(node.right, node0, node1)
        if right_status.num_target_nodes == 2:
            return right_status
        num_target_nodes = (left_status.num_target_nodes
                            + right_status.num_target_nodes
                            + (node0, node1).count(node))
        return Status(num_target_nodes,
                      node if num_target_nodes == 2 else None)
    return lca_helper(tree, node0, node1).ancestor


def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    # return lca_v1(tree, node0, node1)
    return lca_v2(tree, node0, node1)


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    TestLowestCommonAncestor(lca_v1).run_tests()
    TestLowestCommonAncestor(lca_v2).run_tests()
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
