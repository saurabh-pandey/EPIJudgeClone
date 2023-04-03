import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from tests.test_replace_and_remove import TestReplaceAndRemove


def replace_and_remove_v1(size: int, s: List[str]) -> int:
    '''
    My O(1) version
    '''
    def right_shift(s, start, end):
        for i in range(end - 1, start, -1):
            s[i] = s[i - 1]
    
    def left_shift(s, start, end):
        for i in range(start, end):
            s[i] = s[i + 1]
    
    start = 0
    end = size
    while start < end:
        if s[start] == "a":
            end += 1
            right_shift(s, start, end)
            s[start] = "d"
            s[start + 1] = "d"
            start += 2
        elif s[start] == "b":
            left_shift(s, start, end)
            end -= 1
        else:
            start += 1
    return end

def replace_and_remove(size: int, s: List[str]) -> int:
    # TODO - you fill in here.
    return 0


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    TestReplaceAndRemove(replace_and_remove_v1).run_tests()
    # exit(
    #     generic_test.generic_test_main('replace_and_remove.py',
    #                                    'replace_and_remove.tsv',
    #                                    replace_and_remove_wrapper))
