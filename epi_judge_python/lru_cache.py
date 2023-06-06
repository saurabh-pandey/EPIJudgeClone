from typing import Dict, List, Optional, Union

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
        print(f"  node {node.price}, prev = {node.prev}, next = {node.next} ")
        print(f"  head {self._head}, tail = {self._tail}")
        node.next = self._head
        if self._head:
            print(f"  head {self._head.price}")
            print(f"  head.prev {self._head.prev}")
            self._head.prev = node
        self._head = node
        n = self._head
        while n:
            print(f"Forward {n} -> {n.price}")
            n = n.next
        n = self._tail
        while n:
            print(f"Reverse {n} -> {n.price}")
            n = n.prev
        print("  so far = ", self)
        if self._head is self._tail:
            self._tail = self._head.next
        elif not self._tail:
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
        # else:
        #     print(f"  node = {node.price}")
        #     node.prev.next = node.next
        #     node.next.prev = node.prev
    
    def promote(self, node: Node) -> None:
        '''
        Promote a node to the head of list
        '''
        if (node is self._head) or (self._head is self._tail):
            # print("  promote case 1")
            return
        if node is self._tail:
            # print("  promote case 2")
            # print("  1 ", self)
            # print(f"  node {node.price}, prev = {node.prev}, next = {node.next} ")
            self._tail = node.prev
            node.prev.next = None
            node.next = self._head
            self._head.prev = node
            node.prev = None
            self._head = node
        else:
            # print("  promote case 3")
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self._head
            self._head.prev = node
            node.prev = None
            self._head = node
    
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
    
    def evict(self) -> Optional[Node]:
        '''
        Remove last item in the list
        '''
        tail = self._tail
        self.remove(self._tail)
        return tail


class LruCacheV1:
    '''
    My version of the LRU Cache using Hash Table and Doubly Linked List
    '''
    def __init__(self, capacity: int) -> None:
        self._capacity: int = capacity
        self._table: Dict[str, Node] = {}
        self._list: DoublyLinkedList = DoublyLinkedList()
    
    def lookup(self, isbn: int) -> int:
        print("begin lookup => ", self._list)
        if isbn in self._table:
            node = self._table[isbn]
            self._list.promote(node)
            print("end lookup => ", self._list)
            return node.price
        print("end lookup => ", self._list)
        return -1
    
    def insert(self, isbn: int, price: int) -> None:
        print("begin insert => ", self._list)
        if isbn in self._table:
            print("  case 1")
            node = self._table[isbn]
            node.price = price
            self._list.promote(node)
        else:
            print("  case 2")
            if len(self._table) == self._capacity:
                print("    case 2.1 evicted")
                tail = self._list.evict()
                del self._table[tail.isbn]
            node = Node(isbn, price)
            self._table[isbn] = node
            self._list.add(node)
        print("end insert => ", self._list)
            
    def erase(self, isbn: int) -> bool:
        print("begin erase => ", self._list)
        if isbn in self._table:
            node = self._table[isbn]
            self._list.remove(node)
            del self._table[isbn]
            print("end erase => ", self._list)
            return True
        print("end erase => ", self._list)
        return False


def lru_cache_tester(commands, lru_cache_cls = LruCacheV1):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = lru_cache_cls(commands[0][1])

    for cmd in commands[1:]:
        print(cmd)
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


if __name__ == '__main__':
    TestLruCache(v1_lru_cache_tester).run_tests()
    # exit(
    #     generic_test.generic_test_main('lru_cache.py', 'lru_cache.tsv',
    #                                    lru_cache_tester))
