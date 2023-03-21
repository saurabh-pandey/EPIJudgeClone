from tests.test_base import TestBase

from typing import List


class TestIntAsArrayIncrement(TestBase):
    def _int_as_array(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        digits = []
        while n:
            digits.append(n % 10)
            n //= 10
        digits.reverse()
        return digits

    def test_example1(self):
        for i in range(20001):
            A = self._int_as_array(i)
            expected = self._int_as_array(i + 1)
            assert self.solve(A) == expected
