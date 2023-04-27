from tests.test_base import TestBase
from tests.utils import binary_tree

from binary_tree_node import BinaryTreeNode as N


class TestLowestCommonAncestor(TestBase):
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
        node0 = binary_tree.find_node(tree, 7)
        node1 = binary_tree.find_node(tree, 5)
        expected = binary_tree.find_node(tree, 2)
        result = self.solve(tree, node0, node1)
        assert result is expected, (
            f"expected = {expected.data}, result = {result.data}")
