from tests.test_base import TestBase

class TestReverseWords(TestBase):
    def test_example1(self):
        s = "Alice likes Bob"
        expected = "Bob likes Alice"
        s_list = list(s)
        self.solve(s_list)
        assert s_list == list(expected)
    
    def test_single(self):
        s = "Alice"
        expected = "Alice"
        s_list = list(s)
        self.solve(s_list)
        assert s_list == list(expected)
    
    def test_double(self):
        s = "Alice Bob"
        expected = "Bob Alice"
        s_list = list(s)
        self.solve(s_list)
        assert s_list == list(expected)
    