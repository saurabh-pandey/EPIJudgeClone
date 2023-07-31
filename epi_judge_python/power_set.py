import math

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


def generate_power_set_v3(input_set: List[int]) -> List[List[int]]:
    '''
    Simpler brute force version
    '''
    power_set: List[List[int]] = [[]]
    for s in input_set:
        prev_power_set = power_set[:]
        for subset in prev_power_set:
            new_subset = subset[:] + [s]
            power_set.append(new_subset)
    return power_set


def generate_power_set_v4(input_set: List[int]) -> List[List[int]]:
    '''
    Book's final version
    '''
    power_set: List[List[int]] = []
    for int_for_subset in range(1 << len(input_set)):
        bit_array = int_for_subset
        subset = []
        while bit_array:
            subset.append(input_set[int(math.log2(bit_array
                                                  & ~(bit_array - 1)))])
            bit_array &= (bit_array - 1)
        power_set.append(subset)
    return power_set


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    # return generate_power_set_v1(input_set)
    # return generate_power_set_v2(input_set)
    # return generate_power_set_v3(input_set)
    return generate_power_set_v4(input_set)


if __name__ == '__main__':
    TestPowerSet(generate_power_set_v1).run_tests()
    TestPowerSet(generate_power_set_v2).run_tests()
    TestPowerSet(generate_power_set_v3).run_tests()
    TestPowerSet(generate_power_set_v4).run_tests()
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
