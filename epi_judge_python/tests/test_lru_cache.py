from tests.test_base import TestBase

class TestLruCache(TestBase):
    def test_example1(self):
        commands = [["LruCache", 3], ["insert", 0, 10], ["insert", 1, 11],
                    ["lookup", 0, 10], ["lookup", 1, 11], ["erase", 2, 0],
                    ["erase", 1, 1], ["lookup", 1, -1], ["lookup", 0, 10], ["erase", 1, 0], ["insert", 1, 11], ["lookup", 1, 11], ["erase", 1, 1], ["erase", 0, 1], ["lookup", 1, -1], ["lookup", 0, -1], ["insert", 0, 10], ["insert", 1, 11],
                    ["insert", 2, 12], ["lookup", 0, 10], ["lookup", 1, 11],
                    ["lookup", 2, 12], ["lookup", 3, -1], ["insert", 3, 13],
                    ["lookup", 0, -1], ["lookup", 1, 11], ["insert", 2, 12],
                    ["lookup", 3, 13], ["lookup", 1, 11], ["insert", 4, 14],
                    ["lookup", 2, -1], ["lookup", 1, 11], ["insert", 3, 13],
                    ["lookup", 4, 14], ["lookup", 5, -1], ["erase", 4, 1],
                    ["erase", 3, 1], ["erase", 5, 0], ["lookup", 1, 11],
                    ["lookup", 2, -1], ["lookup", 3, -1], ["lookup", 4, -1]]
        self.solve(commands)
    
    def test_attempt1(self):
        commands = [["LruCache", 3, 0], ["insert", 5, 623], ["lookup", 5, 623], 
                    ["erase", 1, 0], ["lookup", 4, -1], ["lookup", 6, -1], 
                    ["insert", 4, 981], ["insert", 5, 550], ["lookup", 2, -1], 
                    ["lookup", 5, 623], ["erase", 3, 0]]
        self.solve(commands)
