from typing import List

from test_framework import generic_test, test_utils

from tests.test_power_set import TestPowerSet


def generate_power_set_v1(input_set: List[int]) -> List[List[int]]:
    '''
    My version
    '''
    def combination(A: List[int], size: int) -> List[List[int]]:
        def combination_recursive(index: int) -> None:
            if len(combi) == size:
                combinations.append(combi[:])
                return
            for i in range(index, len(A)):
                combi.append(A[i])
                combination_recursive(i + 1)
                combi.pop()
        combinations = []
        combi = []
        combination_recursive(0)
        return combinations
    power_set = [[]]
    for sz in range(1, len(input_set) + 1):
        power_set.extend(combination(input_set, sz))
    return power_set


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    return generate_power_set_v1(input_set)


if __name__ == '__main__':
    TestPowerSet(generate_power_set_v1).run_tests()
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
