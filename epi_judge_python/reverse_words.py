import functools

from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from tests.test_reverse_words import TestReverseWords


def reverse_words_v1(s: List[str]) -> None:
    '''
    My version
    '''
    def reverse_in_range(s: List[str], start: int, end: int) -> None:
        x, y = start, end - 1
        while x < y:
            s[x], s[y] = s[y], s[x]
            x += 1
            y -= 1
    
    i, j = 0, len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    start = 0
    for i in range(len(s)):
        if s[i] == " ":
            reverse_in_range(s, start, i)
            start = i + 1
    reverse_in_range(s, start, len(s))

# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    reverse_words_v1(s)


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    TestReverseWords(reverse_words_v1).run_tests()
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
