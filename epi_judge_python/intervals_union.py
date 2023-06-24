import collections
import functools

from dataclasses import dataclass
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

from tests.test_intervals_union import TestIntervalUnion


OldEndpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))
Interval = collections.namedtuple('Interval', ('left', 'right'))

@dataclass
class Endpoint:
    is_closed: bool
    val: int

left_interval_map = {"(": False, "[": True}
right_interval_map = {")": False, "]": True}


def union_of_intervals_v1(intervals: List[Interval]) -> List[Interval]:
    '''
    My version
    '''
    def is_less(ep0: Endpoint, ep1: Endpoint) -> bool:
        if ep0.val < ep1.val:
            return True
        if (ep0.val == ep1.val
        and ep0.is_closed == False and ep1.is_closed == True):
            return True
        return False
    
    def is_equal(ep0: Endpoint, ep1: Endpoint) -> bool:
        if ep0.val != ep1.val:
            return False
        if not ep0.is_closed and not ep1.is_closed:
            return False
        return True
    
    if not intervals:
        return []
    intervals.sort(key=lambda i: (i.left.val,
                                  not i.left.is_closed,
                                  i.right.val,
                                  i.right.is_closed))
    union_intervals = [
        Interval(
            Endpoint(intervals[0].left.is_closed, intervals[0].left.val),
            Endpoint(intervals[0].right.is_closed, intervals[0].right.val)
        )
    ]
    for interval in intervals[1:]:
        curr_interval = union_intervals[-1]
        if (curr_interval.left.val == interval.left.val
        and (curr_interval.left.is_closed or interval.left.is_closed)):
            curr_interval.left.is_closed = True
        if (is_less(interval.left, curr_interval.right)
        or  is_equal(interval.left, curr_interval.right)):
            if is_less(curr_interval.right, interval.right):
                curr_interval.right.val = interval.right.val
                curr_interval.right.is_closed = interval.right.is_closed
        else:
            union_intervals.append(Interval(
                Endpoint(interval.left.is_closed, interval.left.val),
                Endpoint(interval.right.is_closed, interval.right.val)
            ))
    return union_intervals


def union_of_intervals(intervals: List[Interval]) -> List[Interval]:
    return union_of_intervals_v1(intervals)


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
    parsed_intervals: List[Interval] = []
    for interval in intervals:
        assert interval[0] in left_interval_map, f"Incorrect left braces"
        assert interval[-1] in right_interval_map, f"Incorrect right braces"
        is_left_bracket_closed = left_interval_map[interval[0]]
        is_right_bracket_closed = right_interval_map[interval[-1]]
        num_pair_strs = interval[1:-1].split(",")
        assert len(num_pair_strs) == 2, f"Expecting 2 num pairs as interval"
        left_num = int(num_pair_strs[0].strip())
        right_num = int(num_pair_strs[1].strip())
        left_endpoint = Endpoint(is_left_bracket_closed, left_num)
        right_endpoint = Endpoint(is_right_bracket_closed, right_num)
        parsed_intervals.append(Interval(left_endpoint, right_endpoint))
    return parsed_intervals


def interval_to_str(intervals: List[Interval]) -> List[str]:
    '''
    Parse intervals in string and convert to Interval
    '''
    str_intervals: List[str] = []
    for interval in intervals:
        left_bracket = "[" if interval.left.is_closed else "("
        right_bracket = "]" if interval.right.is_closed else ")"
        str_intervals.append(f"{left_bracket}{str(interval.left.val)}, "
                             f"{str(interval.right.val)}{right_bracket}")
    return str_intervals


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
