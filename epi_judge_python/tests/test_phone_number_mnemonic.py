import itertools
import random

from typing import List

from tests.test_base import TestBase


class TestPhoneNumberMnemonic(TestBase):
    PHONE_NUM_CHAR_MAP = ["0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS",
                          "TUV", "WXYZ"]
    
    def expected_mnemonic(self, phone_number: str) -> List[str]:
        digits = [int(c) for c in phone_number]
        chars = [TestPhoneNumberMnemonic.PHONE_NUM_CHAR_MAP[i] for i in digits]
        expected = []
        for prod in itertools.product(*chars):
            expected.append("".join(prod))
        return expected
    
    def test_example1(self):
        phone_number = "23"
        result = self.solve(phone_number)
        expected = self.expected_mnemonic(phone_number)
        assert result == expected, f"Result {result} != {expected} expected"
    
    def test_example2(self):
        phone_number = "023"
        result = self.solve(phone_number)
        expected = self.expected_mnemonic(phone_number)
        assert result == expected, f"Result {result} != {expected} expected"
    
    def test_example3(self):
        phone_number = "123"
        result = self.solve(phone_number)
        expected = self.expected_mnemonic(phone_number)
        assert result == expected, f"Result {result} != {expected} expected"
    
    def test_example4(self):
        phone_number = "0123"
        result = self.solve(phone_number)
        expected = self.expected_mnemonic(phone_number)
        assert result == expected, f"Result {result} != {expected} expected"
    
    def test_example5(self):
        phone_number = "012113"
        result = self.solve(phone_number)
        expected = self.expected_mnemonic(phone_number)
        assert result == expected, f"Result {result} != {expected} expected"
    
    def test_random(self):
        for _ in range(10000):
            phone_number = str(random.randint(0, 100000))
            result = self.solve(phone_number)
            expected = self.expected_mnemonic(phone_number)
            assert result == expected, f"Result {result} != {expected} expected"
