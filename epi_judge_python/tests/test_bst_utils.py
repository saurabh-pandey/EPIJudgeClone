from typing import Optional

from bst_node import BstNode

from tests.test_base import TestBase
from tests.utils import bst


class TestBstUtils(TestBase):
    def test_single_node(self):
        tree = bst.Factory.single_node(BstNode)
        max_depth = bst.max_depth(tree)
        assert max_depth == 1
    
    def test_simple_even(self):
        tree = bst.Factory.simple_even(BstNode)
        max_depth = bst.max_depth(tree)
        assert max_depth == 2
    
    def test_left_leaning(self):
        tree = bst.Factory.left_leaning(BstNode)
        max_depth = bst.max_depth(tree)
        assert max_depth == 2
    
    def test_right_leaning(self):
        tree = bst.Factory.right_leaning(BstNode)
        max_depth = bst.max_depth(tree)
        assert max_depth == 2
    
    def test_three_layered(self):
        tree = bst.Factory.three_layered(BstNode)
        max_depth = bst.max_depth(tree)
        assert max_depth == 3
    
    def test_three_depth_1(self):
        tree = bst.Factory.three_depth_1(BstNode)
        max_depth = bst.max_depth(tree)
        assert max_depth == 3
    
    def test_three_depth_2(self):
        tree = bst.Factory.three_depth_2(BstNode)
        max_depth = bst.max_depth(tree)
        assert max_depth == 3
    
    def test_three_depth_3(self):
        tree = bst.Factory.three_depth_3(BstNode)
        max_depth = bst.max_depth(tree)
        assert max_depth == 3
    
    def test_three_depth_4(self):
        tree = bst.Factory.three_depth_4(BstNode)
        max_depth = bst.max_depth(tree)
        assert max_depth == 3
    
    def test_empty(self):
        tree = None
        max_depth = bst.max_depth(tree)
        assert max_depth == 0
