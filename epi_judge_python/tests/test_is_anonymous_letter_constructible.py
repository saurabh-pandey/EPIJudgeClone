import collections
import random
import string

from tests.test_base import TestBase


class TestIsLetterConstructible(TestBase):
    def test_ascii(self):
        for letter_text, magazine_text in zip(
                self._generate_text(string.ascii_letters, 10, 20),
                self._generate_text(string.ascii_letters, 100, 200)):
            letter_char_freq = collections.Counter(letter_text)
            mag_char_freq = collections.Counter(magazine_text)
            expected = any(
                letter_char_freq[c] > mag_char_freq[c]
                for c in letter_char_freq)
            result = self.solve(letter_text, magazine_text)
            assert expected == result, f"Expected {expected}, result {result}"
    
    def test_mismatch(self):
        for letter_text, magazine_text in zip(
                self._generate_text(string.printable, 10, 20),
                self._generate_text(string.ascii_letters, 100, 200)):
            letter_char_freq = collections.Counter(letter_text)
            mag_char_freq = collections.Counter(magazine_text)
            expected = any(
                letter_char_freq[c] > mag_char_freq[c]
                for c in letter_char_freq)
            result = self.solve(letter_text, magazine_text)
            assert expected == result, f"Expected {expected}, result {result}"
    
    def test_printable(self):
        for letter_text, magazine_text in zip(
                self._generate_text(string.printable, 10, 20),
                self._generate_text(string.printable, 100, 200)):
            letter_char_freq = collections.Counter(letter_text)
            mag_char_freq = collections.Counter(magazine_text)
            expected = any(
                letter_char_freq[c] > mag_char_freq[c]
                for c in letter_char_freq)
            result = self.solve(letter_text, magazine_text)
            assert expected == result, f"Expected {expected}, result {result}"
    

    def _generate_text(self,
                       input_chars: str,
                       min_size: int,
                       max_size: int):
        for unique_chars_len in range(10, len(input_chars)):
            unique_chars = set()
            while len(unique_chars) < unique_chars_len:
                unique_chars.add(
                    input_chars[random.randint(0, len(input_chars))])
            letter_chars = list(unique_chars)
            letter_text = []
            for size in range(min_size, max_size):
                for _ in range(size):
                    letter_text.append(
                        letter_chars[random.randint(0, len(letter_chars))])
                yield "".join(letter_text)
