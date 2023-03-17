from tests.test_base import TestBase

class TestUniformRandomNumber(TestBase):
    def test_example1(self):
        num_trials = 100
        for a in range(0, 10):
            for b in range(a + 1, 201):
                for i in range(num_trials):
                    rand_num = self.solve(a, b)
                    assert (rand_num >= a) and (rand_num <= b)
