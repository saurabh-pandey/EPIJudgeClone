from typing import List

from test_framework import generic_test, test_utils

from tests.test_power_set import TestPowerSet


def generate_power_set_v1(input_set: List[int]) -> List[List[int]]:
    '''
    My version using combination for each size
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
    power_set = []
    for sz in range(0, len(input_set) + 1):
        power_set.extend(combination(input_set, sz))
    return power_set


def generate_power_set_v2(input_set: List[int]) -> List[List[int]]:
    '''
    Book's brute force version
    '''
    def directed_power_set(to_be_selected, selected_so_far):
        if to_be_selected == len(input_set):
            power_set.append(selected_so_far)
            return
        directed_power_set(to_be_selected + 1, selected_so_far)
        directed_power_set(to_be_selected + 1,
                           selected_so_far + [input_set[to_be_selected]])
    
    power_set: List[List[int]] = []
    directed_power_set(0, [])
    return power_set


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    # return generate_power_set_v1(input_set)
    return generate_power_set_v2(input_set)


if __name__ == '__main__':
    TestPowerSet(generate_power_set_v1).run_tests()
    TestPowerSet(generate_power_set_v2).run_tests()
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
