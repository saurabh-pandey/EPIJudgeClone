import collections

from typing import Dict, List, Optional, OrderedDict, Union

from test_framework import generic_test
from test_framework.test_failure import TestFailure

from tests.test_lru_cache import TestLruCache


class Node:
    def __init__(self, isbn: int, price: int) -> None:
        self.isbn: int = isbn
        self.price: int = price
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
    
    def add(self, node: Node) -> None:
        '''
        Add a new Node
        '''
        node.next = self._head
        if self._head:
            self._head.prev = node
        self._head = node
        if not self._tail:
            self._tail = node
    
    def remove(self, node: Node) -> None:
        '''
        Remove an existing node
        '''
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node is self._head:
            self._head = node.next
        if node is self._tail:
            self._tail = node.prev
        node.next = None
        node.prev = None
    
    def promote(self, node: Node) -> None:
        '''
        Promote a node to the head of list
        '''
        if (node is self._head) or (self._head is self._tail):
            return
        self.remove(node)
        self.add(node)
    
    def evict(self) -> Optional[Node]:
        '''
        Remove last item in the list
        '''
        tail = self._tail
        self.remove(self._tail)
        return tail
    
    def __str__(self) -> str:
        forward_cache_order = []
        node = self._head
        while node:
            forward_cache_order.append(str(node.price))
            node = node.next
        reverse_cache_order = []
        node = self._tail
        while node:
            reverse_cache_order.append(str(node.price))
            node = node.prev
        head_str = f"head = {self._head.price if self._head else 'None'}"
        tail_str = f"tail = {self._tail.price if self._tail else 'None'}"
        forward_str = ",".join(forward_cache_order)
        reverse_str = ",".join(reverse_cache_order)
        return (head_str + ", " + tail_str + ", forward = " + forward_str
                + ", reverse = " + reverse_str )


class LruCacheV1:
    '''
    My version of the LRU Cache using Hash Table and Doubly Linked List
    '''
    def __init__(self, capacity: int) -> None:
        self._capacity: int = capacity
        self._table: Dict[str, Node] = {}
        self._list: DoublyLinkedList = DoublyLinkedList()
    
    def lookup(self, isbn: int) -> int:
        if isbn in self._table:
            node = self._table[isbn]
            self._list.promote(node)
            return node.price
        return -1
    
    def insert(self, isbn: int, price: int) -> None:
        if isbn in self._table:
            node = self._table[isbn]
            self._list.promote(node)
        else:
            if len(self._table) == self._capacity:
                tail = self._list.evict()
                del self._table[tail.isbn]
            node = Node(isbn, price)
            self._table[isbn] = node
            self._list.add(node)
            
    def erase(self, isbn: int) -> bool:
        if isbn in self._table:
            node = self._table[isbn]
            self._list.remove(node)
            del self._table[isbn]
            return True
        return False
    
    def __str__(self) -> str:
        list_str = str(self._list)
        dict_str = []
        for isbn, node in self._table.items():
            dict_str.append(f"({isbn}, {node.price})")
        return f"List = {list_str}\nDict = {dict_str}"


class LruCacheV2:
    '''
    Book's version of LRU Cache using OrderedDict
    '''
    def __init__(self, capacity: int) -> None:
        self._isbn_price_table: OrderedDict[
            int, int] = collections.OrderedDict()
        self._capacity: int = capacity
    
    def insert(self, isbn: int, price: int) -> None:
        if isbn in self._isbn_price_table:
            price = self._isbn_price_table.pop(isbn)
        elif len(self._isbn_price_table) == self._capacity:
            self._isbn_price_table.popitem(last=False)
        self._isbn_price_table[isbn] = price
    
    def erase(self, isbn: int) -> bool:
        return self._isbn_price_table.pop(isbn, None) is not None
    
    def lookup(self, isbn: int) -> int:
        if isbn not in self._isbn_price_table:
            return -1
        price = self._isbn_price_table.pop(isbn)
        self._isbn_price_table[isbn] = price
        return price


def lru_cache_tester(commands, lru_cache_cls = LruCacheV2):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = lru_cache_cls(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure('Lookup: expected ' + str(cmd[2]) +
                                  ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure('Erase: expected ' + str(cmd[2]) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


def v1_lru_cache_tester(commands: List[List[Union[str, int]]]) -> None:
    lru_cache_tester(commands, LruCacheV1)

def v2_lru_cache_tester(commands: List[List[Union[str, int]]]) -> None:
    lru_cache_tester(commands, LruCacheV2)


if __name__ == '__main__':
    TestLruCache(v1_lru_cache_tester).run_tests()
    TestLruCache(v2_lru_cache_tester).run_tests()
    exit(
        generic_test.generic_test_main('lru_cache.py', 'lru_cache.tsv',
                                       lru_cache_tester))
