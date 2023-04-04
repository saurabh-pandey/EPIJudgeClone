from tests.test_base import TestBase


class TestReplaceAndRemove(TestBase):
    def test_example1(self):
        s = ['a', 'c', 'd', 'b', 'b', 'c', 'a', '', '']
        size = 7
        expected_s = ['d', 'd', 'c', 'd', 'c', 'd', 'd']
        expected_size = 7
        result = self.solve(size, s)
        assert result == expected_size
        assert s[:result] == expected_s
    
    def test_only_a(self):
        s = ['a', 'a', 'a', '', '', '']
        size = 3
        expected_s = ['d', 'd', 'd', 'd', 'd', 'd']
        expected_size = 6
        result = self.solve(size, s)
        assert result == expected_size
        assert s[:result] == expected_s
    
    def test_only_b(self):
        s = ['b', 'b', 'b', '', '', '']
        size = 3
        expected_s = []
        expected_size = 0
        result = self.solve(size, s)
        assert result == expected_size
        assert s[:result] == expected_s
    
    def test_none_a_b(self):
        s = ['c', 'c', 'd', 'e', 'f', 'g']
        size = 6
        expected_s = ['c', 'c', 'd', 'e', 'f', 'g']
        expected_size = 6
        result = self.solve(size, s)
        assert result == expected_size
        assert s[:result] == expected_s
