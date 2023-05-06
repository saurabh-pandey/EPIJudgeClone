import functools
from typing import List, Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from tests.test_lowest_common_ancestor_with_parent import (
    TestLowestCommonAncestorWithParent)


def lca_v1(node0: BinaryTreeNode,
           node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    '''
    This version uses stack and path intersection to find LCA. O(h) in time and 
    space
    '''
    def get_root_path(node: BinaryTreeNode) -> List[BinaryTreeNode]:
        path = []
        while node:
            path.append(node)
            node = node.parent
        return path
    path0 = get_root_path(node0)
    path1 = get_root_path(node1)
    matching = None
    while path0 and path1 and (path0[-1] is path1[-1]):
        matching = path0[-1]
        path0.pop()
        path1.pop()
    return matching


def lca_v2(node0: BinaryTreeNode,
           node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    '''
    This version use a hash table and again has O(h) time and space complexity
    '''
    node = node0
    nodes_in_path = set()
    while node:
        nodes_in_path.add(node)
        node = node.parent
    node = node1
    while node not in nodes_in_path:
        node = node.parent
    return node


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
    TestLowestCommonAncestorWithParent(lca_v1).run_tests()
    TestLowestCommonAncestorWithParent(lca_v2).run_tests()
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
