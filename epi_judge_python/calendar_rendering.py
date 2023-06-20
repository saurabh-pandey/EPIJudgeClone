import bisect
import collections
import functools

from typing import List, Tuple

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

from tests.test_calendar_rendering import TestCalendarRendering


# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events_v1(A: List[Event]) -> int:
    '''
    My version with O(n) space O(nlog(n)) time complexity
    TODO: In newer python version we can use a reverse sorted end_times list
    and then end_times.pop() can happen from the end which would be faster.
    '''
    if not A:
        return 0
    A.sort(key=lambda a: a.start)
    max_simultaneous = 1
    end_times = [A[0].finish]
    for b, e in A[1:]:
        if b <= end_times[0]:
            bisect.insort_left(end_times, e)
            max_simultaneous = max(max_simultaneous, len(end_times))
        else:
            while end_times and b > end_times[0]:
                end_times.pop(0)
            bisect.insort_left(end_times, e)
    return max_simultaneous


def find_max_simultaneous_events_v2(A: List[Event]) -> int:
    '''
    Book's solution with same complexity
    '''
    EndPoint = collections.namedtuple('EndPoint', ['time', 'is_start'])
    endpoints: List[EndPoint] = [
        point for e in A for point in (EndPoint(e.start, True),
                                       EndPoint(e.finish, False))]
    endpoints.sort(key=lambda p: (p.time, not p.is_start))
    max_simultaneous = 0
    num_simultaneous = 0
    for e in endpoints:
        if e.is_start:
            num_simultaneous += 1
            max_simultaneous = max(max_simultaneous, num_simultaneous)
        else:
            num_simultaneous -= 1
    return max_simultaneous


def find_max_simultaneous_events(A: List[Event]) -> int:
    # return find_max_simultaneous_events_v1(A)
    return find_max_simultaneous_events_v2(A)


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


def find_max_simultaneous_events_wrapper_v1(A: List[Tuple[int, int]]) -> int:
    events = [Event(*x) for x in A]
    return find_max_simultaneous_events_v1(events)


def find_max_simultaneous_events_wrapper_v2(A: List[Tuple[int, int]]) -> int:
    events = [Event(*x) for x in A]
    return find_max_simultaneous_events_v2(events)


if __name__ == '__main__':
    TestCalendarRendering(find_max_simultaneous_events_wrapper_v1).run_tests()
    TestCalendarRendering(find_max_simultaneous_events_wrapper_v2).run_tests()
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
