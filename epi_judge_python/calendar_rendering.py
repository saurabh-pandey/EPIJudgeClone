import collections
import functools
from typing import List, Tuple

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

from tests.test_calendar_rendering import TestCalendarRendering


# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events_v1(A: List[Tuple[int, int]]) -> int:
    '''
    My version
    '''
    return 0


def find_max_simultaneous_events(A: List[Event]) -> int:
    # TODO - you fill in here.
    return 0


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    TestCalendarRendering(find_max_simultaneous_events_v1).run_tests()
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
