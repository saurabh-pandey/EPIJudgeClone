import random

from tests.test_base import TestBase


class TestAbsentValue(TestBase):
    def test_random(self):
        ip_max = (1 << 32) - 1
        ips = set()
        for _ in range(1, 2000):
            ips.add(random.randint(0, ip_max))
            result = self.solve(iter(ips))
            assert result not in ips, f"{result} is not correct"
