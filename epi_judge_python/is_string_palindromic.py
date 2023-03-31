from test_framework import generic_test
from tests.test_is_string_palindromic import TestIsStringPalindromic


def is_palindromic_v1(s: str) -> bool:
    '''
    My O(1) version
    '''
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def is_palindromic(s: str) -> bool:
    return is_palindromic_v1(s)


if __name__ == '__main__':
    TestIsStringPalindromic(is_palindromic_v1).run_tests()
    exit(
        generic_test.generic_test_main('is_string_palindromic.py',
                                       'is_string_palindromic.tsv',
                                       is_palindromic))
