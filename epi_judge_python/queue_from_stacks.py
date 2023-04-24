from test_framework import generic_test
from test_framework.test_failure import TestFailure

from tests.test_queue_from_stacks import TestQueueFromStack

class QueueV1:
    '''
    My version with O(1) enqueue and O(n) dequeue
    '''
    def __init__(self) -> None:
        self._push_stack = []
        self._pop_stack = []
    
    def enqueue(self, x: int) -> None:
        self._push_stack.append(x)

    def dequeue(self) -> int:
        while self._push_stack:
            self._pop_stack.append(self._push_stack.pop())
        value = self._pop_stack.pop()
        while self._pop_stack:
            self._push_stack.append(self._pop_stack.pop())
        return value


class QueueV2:
    '''
    Book's version with O(1) enqueue and O(m) dequeue for m dequeue ops
    '''
    def __init__(self) -> None:
        self._enqueue_stack = []
        self._dequeue_stack = []
    
    def enqueue(self, x: int) -> None:
        self._enqueue_stack.append(x)
    
    def dequeue(self) -> int:
        if not self._dequeue_stack:
            while self._enqueue_stack:
                self._dequeue_stack.append(self._enqueue_stack.pop())
        return self._dequeue_stack.pop()

def queue_tester(ops, queue_cls = QueueV2):
    try:
        q = queue_cls()

        for (op, arg) in ops:
            if op == 'Queue':
                q = queue_cls()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


def v1_queue_tester(ops):
    queue_tester(ops, QueueV1)


def v2_queue_tester(ops):
    queue_tester(ops, QueueV1)


if __name__ == '__main__':
    TestQueueFromStack(v1_queue_tester).run_tests()
    TestQueueFromStack(v2_queue_tester).run_tests()
    exit(
        generic_test.generic_test_main('queue_from_stacks.py',
                                       'queue_from_stacks.tsv', queue_tester))
