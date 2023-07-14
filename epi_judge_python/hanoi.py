import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from tests.test_hanoi import TestHanoi


NUM_PEGS = 3

# for pegs 0 and 1 remaining peg is 2 => 0 + 1 maps to 2
# for pegs 1 and 2 remaining peg is 0 => 1 + 2 maps to 0
# for pegs 2 and 0 remaining peg is 1 => 0 + 2 maps to 1
# Above can be stored in an array with index as origin + dest - 1
CYCLIC_PEGS = [2, 1, 0]


def compute_tower_hanoi_v1(num_rings: int) -> List[List[int]]:
    '''
    My version
    '''
    def hanoi_steps(ring: int, origin: int, dest: int) -> List[List[int]]:
        if ring == 0:
            return []
        elif ring == 1:
            return [[origin, dest]]
        steps = []
        remain_peg = CYCLIC_PEGS[origin + dest - 1]
        steps.extend(hanoi_steps(ring - 1, origin, remain_peg))
        steps.append([origin, dest])
        steps.extend(hanoi_steps(ring - 1, remain_peg, dest))
        return steps
    return hanoi_steps(num_rings, 0, 1)

def compute_tower_hanoi(num_rings: int) -> List[List[int]]:
    return compute_tower_hanoi_v1(num_rings)


@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))
            ] + [[] for _ in range(1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure('Illegal move from {} to {}'.format(
                pegs[from_peg][-1], pegs[to_peg][-1]))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure('Pegs doesn\'t place in the right configuration')


if __name__ == '__main__':
    TestHanoi(compute_tower_hanoi_v1).run_tests()
    exit(
        generic_test.generic_test_main('hanoi.py', 'hanoi.tsv',
                                       compute_tower_hanoi_wrapper))
