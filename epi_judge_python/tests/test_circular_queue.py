from tests.test_base import TestBase


class TestCircularQueue(TestBase):
    def test_example1(self):
        operations = [("Queue", 1), ("size", 0), ("enqueue", 0), ("size", 1),
                      ("dequeue", 0), ("size", 0), ("enqueue", 0),
                      ("enqueue", 1), ("size", 2), ("enqueue", 2), ("size", 3),
                      ("enqueue", 3), ("dequeue", 0), ("dequeue", 1),
                      ("size", 2), ("dequeue", 2), ("dequeue", 3), ("size", 0)]
        self.solve(operations)
    
    def test_example2(self):
        operations = [("Queue", 4), ("enqueue", 0), ("enqueue", 1),
                      ("enqueue", 2), ("dequeue", 0), ("enqueue", 3),
                      ("enqueue", 4), ("size", 4), ("dequeue", 1),
                      ("enqueue", 5), ("size", 4), ("dequeue", 2),
                      ("enqueue", 6), ("size", 4), ("dequeue", 3),
                      ("dequeue", 4), ("dequeue", 5), ("dequeue", 6),
                      ("size", 0), ("enqueue", 7), ("enqueue", 8),
                      ("enqueue", 9), ("enqueue", 10), ("enqueue", 11),
                      ("size", 5)]
        self.solve(operations)
    
    def test_example3(self):
        operations = [("Queue", 4), ("enqueue", 0), ("enqueue", 1),
                      ("enqueue", 2), ("size", 3), ("enqueue", 3),
                      ("size", 4), ("enqueue", 4), ("size", 5), ("enqueue", 5),
                      ("enqueue", 6), ("enqueue", 7), ("size", 8),
                      ("enqueue", 8), ("size", 9), ("enqueue", 9), ("size", 10),
                      ("dequeue", 0), ("size", 9), ("dequeue", 1), ("size", 8),
                      ("dequeue", 2), ("dequeue", 3), ("dequeue", 4),
                      ("dequeue", 5), ("dequeue", 6), ("dequeue", 7),
                      ("dequeue", 8), ("dequeue", 9), ("size", 0)]
        self.solve(operations)
