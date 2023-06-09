import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from tests.test_lowest_common_ancestor_close_ancestor import (
    TestLowestCommonAncestorCloseAncestor
)


def lca_v1(node0: BinaryTreeNode,
           node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    '''
    Find LCA using a hash table with O(h) time and space complexity
    '''
    nodes_in_path = set()
    it = node0
    while it:
        nodes_in_path.add(it)
        it = it.parent
    it = node1
    while it not in nodes_in_path:
        it = it.parent
    return it


def lca_v2(node0: BinaryTreeNode,
           node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    '''
    Book's version O(D0 + D1) time and space complexity where D0 and D1 are
    distance from each node to LCA
    '''
    visited_nodes = set()
    it0, it1 = node0, node1
    while it0 or it1:
        if it0:
            if it0 in visited_nodes:
                return it0
            visited_nodes.add(it0)
            it0 = it0.parent
        if it1:
            if it1 in visited_nodes:
                return it1
            visited_nodes.add(it1)
            it1 = it1.parent
    raise ValueError("Node0 and Node1 don't belong to the same tree")


def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    # return lca_v1(node0, node1)
    return lca_v2(node0, node1)


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    TestLowestCommonAncestorCloseAncestor(lca_v1).run_tests()
    TestLowestCommonAncestorCloseAncestor(lca_v2).run_tests()
    exit(
        generic_test.generic_test_main(
            'lowest_common_ancestor_close_ancestor.py',
            'lowest_common_ancestor.tsv', lca_wrapper))
