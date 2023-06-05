from typing import List, Union

from test_framework import generic_test
from test_framework.test_failure import TestFailure

from tests.test_lru_cache import TestLruCache


class LruCacheV1:
    def __init__(self, capacity: int) -> None:
        # TODO - you fill in here.
        return

    def lookup(self, isbn: int) -> int:
        # TODO - you fill in here.
        return 0

    def insert(self, isbn: int, price: int) -> None:
        # TODO - you fill in here.
        return

    def erase(self, isbn: int) -> bool:
        # TODO - you fill in here.
        return True


def lru_cache_tester(commands, lru_cache_cls = LruCacheV1):
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


if __name__ == '__main__':
    TestLruCache(v1_lru_cache_tester).run_tests()
    exit(
        generic_test.generic_test_main('lru_cache.py', 'lru_cache.tsv',
                                       lru_cache_tester))
