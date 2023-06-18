from tests.test_base import TestBase


class TestTwoSortedArraysMerge(TestBase):
    def test_example1(self):
        A = [3, 13, 17, None, None, None, None, None]
        m = 3
        B = [3, 7, 11, 19]
        n = 4
        self.solve(A, m, B, n)
        assert all(A[i - 1] <= A[i] for i in range(1, m + n))
    
    def test_a_before_b(self):
        A = [3, 4, 5, None, None, None, None, None]
        m = 3
        B = [6, 7, 8, 9]
        n = 4
        self.solve(A, m, B, n)
        assert all(A[i - 1] <= A[i] for i in range(1, m + n))
    
    def test_a_after_b(self):
        A = [7, 8, 9, None, None, None, None, None]
        m = 3
        B = [3, 4, 5, 6]
        n = 4
        self.solve(A, m, B, n)
        assert all(A[i - 1] <= A[i] for i in range(1, m + n))
    
    def test_all_equal(self):
        A = [1, 1, 1, None, None, None, None, None]
        m = 3
        B = [1, 1, 1, 1]
        n = 4
        self.solve(A, m, B, n)
        assert all(A[i - 1] <= A[i] for i in range(1, m + n))
    
    def test_only_a(self):
        A = [1, 2, 3, None]
        m = 3
        B = []
        n = 0
        self.solve(A, m, B, n)
        assert all(A[i - 1] <= A[i] for i in range(1, m + n))
    
    def test_only_b(self):
        A = [None, None, None, None, None]
        m = 0
        B = [1, 2, 3, 4]
        n = 4
        self.solve(A, m, B, n)
        assert all(A[i - 1] <= A[i] for i in range(1, m + n))
