from tests.test_base import TestBase


class TestIsStringPermutableToPalindrome(TestBase):
    def test_example(self):
        s = "edified"
        expected = True
        result = self.solve(s)
        assert result == expected, f"Expected {expected}, result {result}"
