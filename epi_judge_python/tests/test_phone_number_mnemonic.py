import itertools

from typing import List

from tests.test_base import TestBase


class TestPhoneNumberMnemonic(TestBase):
    def expected_mnemonic(self, num) -> List[str]:
        # return itertools.product("ABC", "DEF")
        return []
    
    def test_example1(self):
        phone_number = "23"
        result = self.solve(phone_number)
        expected = self.expected_mnemonic(phone_number)
        assert result == expected, f"Result {result} != {expected} expected"
