from list_node import ListNode
from test_framework import generic_test
from tests.test_search_in_list import TestSearchInList


def search_list_v1(L: ListNode, key: int) -> ListNode:
    '''
    My O(n) version
    '''
    curr_node = L
    while curr_node:
        if curr_node.data == key:
            return curr_node
        curr_node = curr_node.next
    return None

def search_list(L: ListNode, key: int) -> ListNode:
    return search_list_v1(L, key)


def search_list_wrapper(L, key):
    result = search_list(L, key)
    return result.data if result else -1


if __name__ == '__main__':
    TestSearchInList(search_list_v1).run_tests()
    exit(
        generic_test.generic_test_main('search_in_list.py',
                                       'search_in_list.tsv',
                                       search_list_wrapper))
