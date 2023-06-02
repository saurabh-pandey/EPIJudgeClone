import collections

from test_framework import generic_test

from tests.test_is_string_permutable_to_palindrome import (
    TestIsStringPermutableToPalindrome
)


def can_form_palindrome_v1(s: str) -> bool:
    '''
    My version with O(n) time and O(c) space where c is number of unique chars
    '''
    char_count = collections.defaultdict(int)
    for c in s:
        char_count[c] += 1
    has_odd_count = False
    for count in char_count.values():
        if count % 2 == 1:
            if has_odd_count:
                return False
            else:
                has_odd_count = True
    return True


def can_form_palindrome_v2(s: str) -> bool:
    '''
    Book's version with same complexity but using Counter
    '''
    return sum(count % 2 for count in collections.Counter(s).values()) <= 1


def can_form_palindrome(s: str) -> bool:
    # return can_form_palindrome_v1(s)
    return can_form_palindrome_v2(s)


if __name__ == '__main__':
    TestIsStringPermutableToPalindrome(can_form_palindrome_v1).run_tests()
    TestIsStringPermutableToPalindrome(can_form_palindrome_v2).run_tests()
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
