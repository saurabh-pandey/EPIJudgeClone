import math
import random

from typing import Optional

from bst_node import BstNode

from tests.test_base import TestBase
from tests.utils import bst

class TestBstFromSortedArray(TestBase):
    def test_unique(self):
        for sz in range(1, 100):
            A = [i for i in range(sz)]
            result: Optional[BstNode] = self.solve(A)
            max_depth = bst.max_depth(result)
            assert math.floor(math.log2(len(A))) + 1 == max_depth, (
                f"Failed for A = {A}")
    
    def test_random(self):
        for sz in range(1, 100):
            A = [random.randint(0, sz) for i in range(sz)]
            A.sort()
            result: Optional[BstNode] = self.solve(A)
            max_depth = bst.max_depth(result)
            assert math.floor(math.log2(len(A))) + 1 == max_depth, (
                f"Failed for A = {A}")
    
    def test_empty(self):
        result = self.solve([])
        assert result is None, f"Result should be None"
