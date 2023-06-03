import collections
import random
import string

from tests.test_base import TestBase


import pdb

class TestIsLetterConstructible(TestBase):
    def test_example1(self):
        letter_text = "112"
        magazine_text = "1123"
        expected = self._check(letter_text, magazine_text)
        result = self.solve(letter_text, magazine_text)
        assert expected == result, f"expected {expected} result {result}"
    
    def test_example2(self):
        letter_text = "112233"
        magazine_text = "1123333445566"
        expected = self._check(letter_text, magazine_text)
        result = self.solve(letter_text, magazine_text)
        assert expected == result, f"expected {expected} result {result}"
    
    def test_empty(self):
        letter_text = ""
        magazine_text = ""
        expected = self._check(letter_text, magazine_text)
        result = self.solve(letter_text, magazine_text)
        assert expected == result, f"expected {expected} result {result}"
    
    def test_equal(self):
        letter_text = "123"
        magazine_text = "123"
        expected = self._check(letter_text, magazine_text)
        result = self.solve(letter_text, magazine_text)
        assert expected == result, f"expected {expected} result {result}"

    def _check(self, letter_text: str, magazine_text: str) -> bool:
        letter_char_freq = collections.Counter(letter_text)
        mag_char_freq = collections.Counter(magazine_text)
        for c in letter_char_freq:
            if c not in mag_char_freq:
                return False
            elif letter_char_freq[c] > mag_char_freq[c]:
                return False
        return True

