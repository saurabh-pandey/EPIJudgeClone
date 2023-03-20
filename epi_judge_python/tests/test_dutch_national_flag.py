from tests.test_base import TestBase

from enum import Enum


class Partition(Enum):
    LESS = 0
    EQUAL = 1
    GREATER = 2

class TestDutchNationalFlag(TestBase):
    def check_partition(self, pivot, A):
        if not A:
            return True
        state = None
        if A[0] < pivot:
            state = Partition.LESS
        elif A[0] == pivot:
            state = Partition.EQUAL
        else:
            state = Partition.GREATER
        for i in range(1, len(A)):
            if A[i] < pivot:
                if state != Partition.LESS:
                    return False
            elif A[i] == pivot:
                if state == Partition.LESS:
                    state = Partition.EQUAL
                elif state == Partition.GREATER:
                    return False
            else:
                if state == Partition.LESS:
                    return False
                elif state == Partition.EQUAL:
                    state = Partition.GREATER
        return True

    def test_example1(self):
        A = [0, 1, 2, 0, 2, 1, 1]
        pivot_index = 3
        pivot = A[pivot_index]
        self.solve(pivot_index, A)
        # print(A)
        assert self.check_partition(pivot, A)
    
    def test_example2(self):
        A = [0, 1, 2, 0, 2, 1, 1]
        pivot_index = 2
        pivot = A[pivot_index]
        self.solve(pivot_index, A)
        # print(A)
        assert self.check_partition(pivot, A)
    
    def test_example3(self):
        A = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
        pivot_index = 2
        pivot = A[pivot_index]
        self.solve(pivot_index, A)
        # print(A)
        assert self.check_partition(pivot, A)
    
    def test_sorted(self):
        A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        pivot_index = 2
        pivot = A[pivot_index]
        self.solve(pivot_index, A)
        # print(A)
        assert self.check_partition(pivot, A)
    
    def test_reverse_sorted(self):
        A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        pivot_index = 4
        pivot = A[pivot_index]
        self.solve(pivot_index, A)
        # print(A)
        assert self.check_partition(pivot, A)
