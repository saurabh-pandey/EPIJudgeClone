import functools
import random
import math

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    check_sequence_is_uniformly_random, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook
from tests.test_uniform_random_number import TestUniformRandomNumber

def zero_one_random():
    return random.randrange(2)


def uniform_random_v1(lower_bound: int, upper_bound: int) -> int:
    '''
    My version
    '''
    diff = upper_bound - lower_bound
    assert diff >= 0
    if diff == 0:
        return lower_bound
    result = diff + 1
    num_bits = math.floor(math.log2(diff)) + 1
    while result > diff:
        rand_num = 0
        for i in range(num_bits):
            rand_num |= (zero_one_random() << i)
        result = rand_num
    return result + lower_bound


def uniform_random_v2(lower_bound: int, upper_bound: int) -> int:
    '''
    Book's version
    '''
    number_of_outcomes = upper_bound - lower_bound + 1
    while True:
        result, i = 0, 0
        while (1 << i) < number_of_outcomes:
            result = (result << 1) | zero_one_random()
            i += 1
        if result < number_of_outcomes:
            break
    return result + lower_bound


def uniform_random(lower_bound: int, upper_bound: int) -> int:
    # return uniform_random_v1(lower_bound, upper_bound)
    return uniform_random_v2(lower_bound, upper_bound)


@enable_executor_hook
def uniform_random_wrapper(executor, lower_bound, upper_bound):
    def uniform_random_runner(executor, lower_bound, upper_bound):
        result = executor.run(
            lambda:
            [uniform_random(lower_bound, upper_bound) for _ in range(100000)])

        return check_sequence_is_uniformly_random(
            [a - lower_bound for a in result], upper_bound - lower_bound + 1,
            0.01)

    run_func_with_retries(
        functools.partial(uniform_random_runner, executor, lower_bound,
                          upper_bound))


if __name__ == '__main__':
    TestUniformRandomNumber(uniform_random_v1).run_tests()
    TestUniformRandomNumber(uniform_random_v2).run_tests()
    exit(
        generic_test.generic_test_main('uniform_random_number.py',
                                       'uniform_random_number.tsv',
                                       uniform_random_wrapper))
