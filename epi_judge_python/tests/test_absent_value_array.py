import random

from tests.test_base import TestBase

class TestAbsentValue(TestBase):
    def test_random(self):
        for size in range(1, 1000):
            ip_max = 1 << 32 - 1
            ips = {random.randint(0, ip_max) for _ in range(size)}
            result = self.solve(iter(ips))
            assert result not in ips, f"{result} is not correct"
