from bst_node import BstNode

class Factory:
    '''
    Factory for some standard Binary Search Trees used in tests
    '''
    @staticmethod
    def single_node() -> BstNode:
        tree = BstNode(1)
        return tree
    
    @staticmethod
    def simple_even() -> BstNode:
        tree = BstNode(4,
            BstNode(2),
            BstNode(6),
        )
        return tree

    @staticmethod
    def left_leaning() -> BstNode:
        tree = BstNode(2,
            BstNode(1)
        )
        return tree
    
    @staticmethod
    def right_leaning() -> BstNode:
        tree = BstNode(2,
            None,
            BstNode(3)
        )
        return tree

    @staticmethod
    def three_layered() -> BstNode:
        tree = BstNode(4,
            BstNode(2,
                BstNode(1),
                BstNode(3)
            ),
            BstNode(6,
                BstNode(5),
                BstNode(7)
            ),
        )
        return tree
