from test_framework import generic_test
from test_framework.test_failure import TestFailure

from tests.test_stack_with_max import TestStackWithMax

class Stack:
    def __init__(self) -> None:
        self._stack = []
        self._max = []
    
    def empty(self) -> bool:
        return True if not self._stack else False

    def max(self) -> int:
        return self._max[-1]

    def pop(self) -> int:
        value = self._stack.pop()
        if self._max[-1] == value:
            self._max.pop()
        return value

    def push(self, x: int) -> None:
        self._stack.append(x)
        if not self._max or x >= self._max[-1]:
            self._max.append(x)


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    TestStackWithMax(stack_tester).run_tests()
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
