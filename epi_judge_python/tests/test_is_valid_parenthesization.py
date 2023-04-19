from tests.test_base import TestBase

class TestIsValidParenthesization(TestBase):
    def test_example1(self):
        s = "{}"
        res = self.solve(s)
        expected = True
        assert res == expected, f"Failed for s = {s}, expected = {expected}"
    
    def test_example2(self):
        s = "{}()[]"
        res = self.solve(s)
        expected = True
        assert res == expected, f"Failed for s = {s}, expected = {expected}"
    
    def test_example3(self):
        s = "[{()}]"
        res = self.solve(s)
        expected = True
        assert res == expected, f"Failed for s = {s}, expected = {expected}"
    
    def test_example4(self):
        s = "[{}]{()}([])"
        res = self.solve(s)
        expected = True
        assert res == expected, f"Failed for s = {s}, expected = {expected}"
    
    def test_example5(self):
        s = "[{()()}]{([][])[]}([{}{}]{}{})"
        res = self.solve(s)
        expected = True
        assert res == expected, f"Failed for s = {s}, expected = {expected}"
    
    def test_example6(self):
        s = "[)"
        res = self.solve(s)
        expected = False
        assert res == expected, f"Failed for s = {s}, expected = {expected}"
    
    def test_example7(self):
        s = "[{()})"
        res = self.solve(s)
        expected = False
        assert res == expected, f"Failed for s = {s}, expected = {expected}"
    
    def test_example8(self):
        s = "[{())]"
        res = self.solve(s)
        expected = False
        assert res == expected, f"Failed for s = {s}, expected = {expected}"
    
    def test_example9(self):
        s = "[{()}]{([})}"
        res = self.solve(s)
        expected = False
        assert res == expected, f"Failed for s = {s}, expected = {expected}"
    
    def test_example10(self):
        s = "["
        res = self.solve(s)
        expected = False
        assert res == expected, f"Failed for s = {s}, expected = {expected}"
    
    def test_example11(self):
        s = "{"
        res = self.solve(s)
        expected = False
        assert res == expected, f"Failed for s = {s}, expected = {expected}"
    
    def test_example12(self):
        s = "[{((()))}"
        res = self.solve(s)
        expected = False
        assert res == expected, f"Failed for s = {s}, expected = {expected}"
    
    def test_error1(self):
        s = "}"
        res = self.solve(s)
        expected = False
        assert res == expected, f"Failed for s = {s}, expected = {expected}"
