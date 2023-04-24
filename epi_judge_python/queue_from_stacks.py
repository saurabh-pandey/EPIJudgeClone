from test_framework import generic_test
from test_framework.test_failure import TestFailure

from tests.test_queue_from_stacks import TestQueueFromStack

class Queue:
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


def queue_tester(ops):
    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
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


if __name__ == '__main__':
    TestQueueFromStack(queue_tester).run_tests()
    # exit(
    #     generic_test.generic_test_main('queue_from_stacks.py',
    #                                    'queue_from_stacks.tsv', queue_tester))
