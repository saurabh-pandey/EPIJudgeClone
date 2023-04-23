from test_framework import generic_test
from test_framework.test_failure import TestFailure

from tests.test_circular_queue import TestCircularQueue


class Queue_V1:
    '''
    My version of circular queue with O(1) time
    '''
    def __init__(self, capacity: int) -> None:
        self._begin = None
        self._end = 0
        self._data = [None for _ in range(capacity)]

    def enqueue(self, x: int) -> None:
        if self._end == self._begin:
            self._resize()
        if self._begin is None:
            self._begin = 0
        self._data[self._end] = x
        self._end += 1
        self._end %= len(self._data)

    def dequeue(self) -> int:
        assert self._begin is not None, "No data to enqueue"
        result = self._data[self._begin]
        self._begin += 1
        self._begin %= len(self._data)
        if self._begin == self._end:
            self._begin = None
            self._end = 0
        return result

    def size(self) -> int:
        if self._begin is None:
            return 0
        elif self._begin < self._end:
            return self._end - self._begin
        elif self._begin == self._end:
            return len(self._data)
        else:
            return len(self._data) - (self._begin - self._end)
    
    def _resize(self, scale_factor: int = 2) -> None:
        new_data = [None for _ in range(scale_factor * len(self._data))]
        new_it = 0
        for i in range(self._begin, len(self._data)):
            new_data[new_it] = self._data[i]
            new_it += 1
        for i in range(0, self._end):
            new_data[new_it] = self._data[i]
            new_it += 1
        self._data = new_data
        self._begin = 0
        self._end = new_it


def queue_tester(ops):
    q = Queue_V1(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue_V1(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    TestCircularQueue(queue_tester).run_tests()
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
