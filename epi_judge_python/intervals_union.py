import collections
import functools

from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

from tests.test_intervals_union import TestIntervalUnion


Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))
Interval = collections.namedtuple('Interval', ('left', 'right'))


def union_of_intervals_v1(intervals: List[Interval]) -> List[Interval]:
    '''
    My version
    '''
    return []


def union_of_intervals(intervals: List[Interval]) -> List[Interval]:
    # TODO - you fill in here.
    return []


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


def str_to_interval(intervals: List[str]) -> List[Interval]:
    '''
    Parse intervals in string and convert to Interval
    '''
    return []

def interval_to_str(intervals: List[Interval]) -> List[str]:
    '''
    Parse intervals in string and convert to Interval
    '''
    return []



def wrapper_union_of_intervals_v1(intervals: List[str]) -> List[str]:
    '''
    Parse intervals in string and convert to Interval
    '''
    # TODO: Is a good place to use decorators?
    parsed_intervals: List[Interval] = str_to_interval(intervals)
    result: List[Interval] = union_of_intervals_v1(parsed_intervals)
    return interval_to_str(result)


if __name__ == '__main__':
    TestIntervalUnion(wrapper_union_of_intervals_v1).run_tests()
    exit(
        generic_test.generic_test_main('intervals_union.py',
                                       'intervals_union.tsv',
                                       union_of_intervals_wrapper))
