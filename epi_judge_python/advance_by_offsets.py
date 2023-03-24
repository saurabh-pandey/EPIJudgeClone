from typing import List

from test_framework import generic_test
from tests.test_advance_by_offsets import TestAdvanceByOffset

def can_reach_end_v1(A: List[int]) -> bool:
    last_index = len(A) - 1
    furthest_reach_index = 0
    i = 0
    while i <= furthest_reach_index and furthest_reach_index < last_index:
        furthest_reach_index = max(i + A[i], furthest_reach_index)
        i += 1
    return furthest_reach_index >= last_index

def can_reach_end(A: List[int]) -> bool:
    return can_reach_end_v1(A)


if __name__ == '__main__':
    TestAdvanceByOffset(can_reach_end_v1).run_tests()
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
