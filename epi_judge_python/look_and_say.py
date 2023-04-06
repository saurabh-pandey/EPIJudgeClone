from test_framework import generic_test
from tests.test_look_and_say import TestLookAndSay


def look_and_say_v1(n: int) -> str:
    '''
    My version
    '''
    pass

def look_and_say(n: int) -> str:
    # TODO - you fill in here.
    return ''


if __name__ == '__main__':
    TestLookAndSay(look_and_say_v1).run_tests()
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
