from tests.test_base import TestBase


class TestLookAndSay(TestBase):
    look_and_say_series = ['1', '11', '21', '1211', '111221', '312211', '13112221', '1113213211', '31131211131221']

    def test_example1(self):
        for i, expected in enumerate(TestLookAndSay.look_and_say_series):
            assert self.solve(i + 1) == expected
