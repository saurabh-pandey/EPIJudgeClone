from tests.test_base import TestBase

from tests.utils import int_as_array

from typing import List


class TestIntAsArrayIncrement(TestBase):
    def test_example1(self):
        for i in range(20001):
            A = int_as_array.convert(i)
            expected = int_as_array.convert(i + 1)
            assert self.solve(A) == expected
