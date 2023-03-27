from tests.test_base import TestBase

from typing import List

import bisect


class TestEnumeratePrimes(TestBase):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
              61, 67, 71, 73, 79, 83, 89, 97]
    
    def _fetch_primes(self, n: int) -> List[int]:
        return (TestEnumeratePrimes.
                primes[:bisect.bisect_right(TestEnumeratePrimes.primes, n)])

    def test_example1(self):
        for n in range(1, 101):
            expected_primes = self._fetch_primes(n)
            assert self.solve(n) == expected_primes
