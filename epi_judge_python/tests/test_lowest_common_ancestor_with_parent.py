from tests.test_base import TestBase
from tests.utils import binary_tree

from binary_tree_with_parent_prototype import BinaryTreeNode as N

class TestLowestCommonAncestorWithParent(TestBase):
    def test_example1(self):
        nodes = [N(i) for i in range(1, 8)]
        nodes[0].left 
        tree = nodes[0]
        node0 = binary_tree.find_node(tree, 7)
        node1 = binary_tree.find_node(tree, 5)
        expected = binary_tree.find_node(tree, 2)
        result = self.solve(tree, node0, node1)
        assert result is expected, (
            f"expected = {expected.data}, result = {result.data}")
