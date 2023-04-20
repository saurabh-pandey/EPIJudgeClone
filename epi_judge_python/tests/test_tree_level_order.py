from tests.test_base import TestBase

from binary_tree_node import BinaryTreeNode as N

class TestTreeLevelOrder(TestBase):
    def test_example1(self):
        tree = N(1,
                 N(2, N(4, None, N(7)), N(5)),
                 N(3, None, N(6, N(9))))
        expected = [[1], [2, 3], [4, 5, 6], [7, 9]]
        actual = self.solve(tree)
        assert expected == actual, f"expected = {expected}, actual = {actual}"
    
    def test_left_sided(self):
        tree = N(1,N(2, N(3, N(4))))
        expected = [[1], [2], [3], [4]]
        actual = self.solve(tree)
        assert expected == actual, f"expected = {expected}, actual = {actual}"

    def test_right_sided(self):
        tree = N(1, None, N(2, None, N(3, None, N(4))))
        expected = [[1], [2], [3], [4]]
        actual = self.solve(tree)
        assert expected == actual, f"expected = {expected}, actual = {actual}"
    
    def test_error1(self):
        tree = None
        expected = []
        actual = self.solve(tree)
        assert expected == actual, f"expected = {expected}, actual = {actual}"
