import collections

from test_framework import generic_test

from tests.test_is_anonymous_letter_constructible import (
    TestIsLetterConstructible)


def is_letter_constructible_from_magazine_v1(letter_text: str,
                                             magazine_text: str) -> bool:
    '''
    My version O(m + n) time with m and n being size of letter and magazine 
    resp. O(c) space where c is number of unique chars in letter.
    '''
    if not letter_text:
        return True
    letter_char_freq = collections.Counter(letter_text)
    magazine_char_counter = collections.Counter()
    chars_found = set()
    for c in magazine_text:
        if c not in chars_found:
            if c in letter_char_freq:
                magazine_char_counter[c] += 1
                if letter_char_freq[c] == magazine_char_counter[c]:
                    chars_found.add(c)
            if len(chars_found) == len(letter_char_freq):
                return True
    return False


def is_letter_constructible_from_magazine_v2(letter_text: str,
                                             magazine_text: str) -> bool:
    '''
    Book's version with similar time and space complexity.
    '''
    letter_char_freq = collections.Counter(letter_text)
    for c in magazine_text:
        if c in letter_char_freq:
            letter_char_freq[c] -= 1
            if letter_char_freq[c] == 0:
                del letter_char_freq[c]
                if not letter_char_freq:
                    return True
    return not letter_char_freq


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    # return is_letter_constructible_from_magazine_v1(letter_text, magazine_text)
    return is_letter_constructible_from_magazine_v2(letter_text, magazine_text)


if __name__ == '__main__':
    TestIsLetterConstructible(
        is_letter_constructible_from_magazine_v1).run_tests()
    TestIsLetterConstructible(
        is_letter_constructible_from_magazine_v2).run_tests()
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
