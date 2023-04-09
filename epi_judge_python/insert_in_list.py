import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from tests.test_insert_in_list import TestInsertInList


def insert_after_v1(node: ListNode, new_node: ListNode) -> None:
    '''
    My version with O(1) time and space complexity
    '''
    new_node.next, node.next = node.next, new_node

# Insert new_node after node.
def insert_after(node: ListNode, new_node: ListNode) -> None:
    # TODO - you fill in here.
    insert_after_v1(node, new_node)

@enable_executor_hook
def insert_list_wrapper(executor, l, node_idx, new_node_data):
    node = l
    for _ in range(node_idx - 1):
        node = node.next
    new_node = ListNode(new_node_data)

    executor.run(functools.partial(insert_after, node, new_node))

    return l


if __name__ == '__main__':
    TestInsertInList(insert_after_v1).run_tests()
    exit(
        generic_test.generic_test_main('insert_in_list.py',
                                       'insert_in_list.tsv',
                                       insert_list_wrapper))
