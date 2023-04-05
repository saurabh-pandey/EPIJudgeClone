from test_framework import generic_test
from tests.test_is_string_palindromic_punctuation import (
    TestIsStringPalindromicPunctuation)


def is_palindrome_v1(s: str) -> bool:
    '''
    My O(1) version
    '''
    i, j = 0, len(s) - 1
    while i < j:
        is_i_alphanum = s[i].isalnum()
        is_j_alphanum = s[j].isalnum()
        if is_i_alphanum and is_j_alphanum:
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        if not is_i_alphanum:
            i += 1
        if not is_j_alphanum:
            j -= 1
    return True

def is_palindrome_v2(s: str) -> bool:
    '''
    Book's O(1) version
    '''
    i, j = 0, len(s) - 1
    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

def is_palindrome(s: str) -> bool:
    # return is_palindrome_v1(s)
    return is_palindrome_v2(s)


if __name__ == '__main__':
    TestIsStringPalindromicPunctuation(is_palindrome_v1).run_tests()
    TestIsStringPalindromicPunctuation(is_palindrome_v2).run_tests()
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
