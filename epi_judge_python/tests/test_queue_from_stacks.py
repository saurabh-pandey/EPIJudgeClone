from tests.test_base import TestBase

class TestQueueFromStack(TestBase):
    def test_example1(self):
        ops = [("enqueue", 0), ("enqueue", 1), ("enqueue", 2), ("enqueue", 3),
               ("dequeue", 0), ("dequeue", 1), ("dequeue", 2), ("dequeue", 3),
               ("enqueue", 0), ("enqueue", 1), ("enqueue", 2), ("enqueue", 3),
               ("dequeue", 0), ("dequeue", 1), ("dequeue", 2), ("dequeue", 3)]
        self.solve(ops)
    
    def test_example2(self):
        ops = [("enqueue", 0), ("enqueue", 1), ("dequeue", 0), ("enqueue", 2),
               ("enqueue", 3), ("dequeue", 1), ("enqueue", 4), ("enqueue", 5), 
               ("dequeue", 2), ("enqueue", 6), ("enqueue", 7), ("dequeue", 3)]
        self.solve(ops)
    
    def test_example3(self):
        ops = [("enqueue", 0), ("dequeue", 0), ("enqueue", 1), ("dequeue", 1),
               ("enqueue", 2), ("dequeue", 2), ("enqueue", 3), ("dequeue", 3), 
               ("enqueue", 4), ("dequeue", 4), ("enqueue", 5), ("dequeue", 5)]
        self.solve(ops)
