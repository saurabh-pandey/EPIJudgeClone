from typing import List

from tests.test_base import TestBase


class TestAnagrams(TestBase):
    def test_example1(self):
        dictionary = ["debitcard", "elvis", "silent", "badcredit", "lives",
                      "freedom", "listen", "levis", "money"]
        expected = [["debitcard", "badcredit"], ["elvis", "lives", "levis"],
                    ["silent", "listen"]]
        result = self.solve(dictionary)
        for res in result:
            res.sort()
        result.sort()
        for e in expected:
            e.sort()
        expected.sort()
        assert result == expected, f"Expected = {expected}, result = {result}"
