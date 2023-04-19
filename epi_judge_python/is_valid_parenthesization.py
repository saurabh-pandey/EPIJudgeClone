from test_framework import generic_test

from tests.test_is_valid_parenthesization import TestIsValidParenthesization


def is_well_formed_v1(s: str) -> bool:
    '''
    My version O(n) time and space version
    '''
    matching_braces = {'{': '}', '(': ')', '[': ']'}
    wellness_stack = []
    for brace in s:
        if brace in matching_braces:
            wellness_stack.append(brace)
        else:
            if (not wellness_stack or
                    matching_braces[wellness_stack.pop()] != brace):
                return False
    return not wellness_stack


def is_well_formed(s: str) -> bool:
    return is_well_formed_v1(s)


if __name__ == '__main__':
    TestIsValidParenthesization(is_well_formed_v1).run_tests()
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
