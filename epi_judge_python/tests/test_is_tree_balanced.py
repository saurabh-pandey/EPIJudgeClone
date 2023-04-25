from tests.test_base import TestBase

from binary_tree_node import BinaryTreeNode as N

class TestIsTreeBalanced(TestBase):
    def test_example1(self):
        tree = N(1,
                N(2,
                  N(4,
                    N(7)),
                  N(5)
                ),
                N(3,
                  N(6)
                ),
               )
        expected = True
        result = self.solve(tree)
        assert result == expected, f"expected = {expected}, result = {result}"
    
    def test_left_skewed(self):
        tree = N(1, N(2, N(3, N(4))))
        expected = False
        result = self.solve(tree)
        assert result == expected, f"expected = {expected}, result = {result}"
    
    def test_right_skewed(self):
        tree = N(1, None, N(2, None, N(3, None, N(4))))
        expected = False
        result = self.solve(tree)
        assert result == expected, f"expected = {expected}, result = {result}"
    
    def test_empty(self):
        tree = None
        expected = True
        result = self.solve(tree)
        assert result == expected, f"expected = {expected}, result = {result}"
    
    def test_single(self):
        tree = N(1)
        expected = True
        result = self.solve(tree)
        assert result == expected, f"expected = {expected}, result = {result}"
    
    def test_unbalanced(self):
        tree = N(1,
                N(2,
                  N(4,
                    N(6)),
                  N(5)
                ),
                N(3)
               )
        expected = False
        result = self.solve(tree)
        assert result == expected, f"expected = {expected}, result = {result}"
