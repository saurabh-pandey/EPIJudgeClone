from tests.test_base import TestBase
from tests.utils import binary_tree


class TestLowestCommonAncestorCloseAncestor(TestBase):
    def test_example1(self):
        tree = binary_tree.Factory.tree2(True)
        node0 = binary_tree.find_node(tree, 7)
        node1 = binary_tree.find_node(tree, 10)
        lca_node = binary_tree.find_node(tree, 2)
        result = self.solve(node0, node1)
        assert result is lca_node, (
            f"Expected = {lca_node.data}, result = {result.data}")
        node0 = binary_tree.find_node(tree, 10)
        node1 = binary_tree.find_node(tree, 6)
        lca_node = binary_tree.find_node(tree, 1)
        result = self.solve(node0, node1)
        assert result is lca_node, (
            f"Expected = {lca_node.data}, result = {result.data}")
