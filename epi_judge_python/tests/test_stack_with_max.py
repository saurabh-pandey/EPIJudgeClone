from tests.test_base import TestBase

class TestStackWithMax(TestBase):
    def test_example1(self):
        operations = [("Stack", None), ("push", 0), ("max", 0), ("push", 1),
                      ("max", 1), ("push", 2), ("max", 2)]
        self.solve(operations)
    
    def test_example2(self):
        operations = [("Stack", None), ("push", 5), ("max", 5), ("push", 4),
                      ("max", 5), ("push", 3), ("max", 5)]
        self.solve(operations)
    
    def test_example3(self):
        operations = [("Stack", None), ("push", 5), ("max", 5), ("push", 4),
                      ("max", 5), ("push", 3), ("max", 5), ("push", 10), 
                      ("max", 10), ("push", 7), ("max", 10), ("push", 6),
                      ("max", 10), ("push", 12), ("max", 12)]
        self.solve(operations)
    
    def test_example4(self):
        operations = [("Stack", None), ("push", 0), ("max", 0), ("push", 1),
                      ("max", 1), ("push", 2), ("max", 2), ("pop", 2), 
                      ("max", 1), ("pop", 1), ("max", 0), ("pop", 0),
                      ("empty", 1)]
        self.solve(operations)
    
    def test_example5(self):
        operations = [("Stack", None), ("push", 7), ("max", 7), ("push", 1),
                      ("max", 7), ("pop", 1), ("max", 7), ("pop", 7), 
                      ("empty", 1), ("push", 6), ("max", 6), ("push", 9),
                      ("max", 9), ("push", 12), ("max", 12), ("push", 10),
                      ("max", 12), ("push", 12), ("max", 12), ("pop", 12), 
                      ("max", 12), ("pop", 10), ("max", 12), ("pop", 12), 
                      ("max", 9)]
        self.solve(operations)
