from typing import List

from tests.test_base import TestBase

class TestHanoi(TestBase):
    NUM_PEGS: int = 3
    
    def steps_count(num_rings: int) -> int:
        num_steps = 0
        for _ in range(num_rings):
            num_steps = 2 * num_steps + 1
        return num_steps
    
    def replay_steps(num_rings: int, steps: List[List[int]]) -> bool:
        pegs: List[List[int]] = [[] for _ in range(TestHanoi.NUM_PEGS)]
        for i in range(num_rings, 0, -1):
            pegs[0].append(i)
        print(f"Pegs before = {pegs}")
        for step in steps:
            if step:
                from_peg, to_peg = step
                if not pegs[from_peg]:
                    return False
                moved_ring = pegs[from_peg].pop()
                if pegs[to_peg] and not (pegs[to_peg][-1] > moved_ring):
                        return False
                pegs[to_peg].append(moved_ring)
        empty_pegs_count = sum(1 for peg in pegs if not peg)
        if num_rings == 0:
            if empty_pegs_count != TestHanoi.NUM_PEGS:
                return False
        elif empty_pegs_count != TestHanoi.NUM_PEGS - 1:
            return False
        for peg in pegs:
            if peg:
                if len(peg) != num_rings:
                    return False
                if any(peg[i] <= peg[i + 1] for i in range(num_rings - 1)):
                    return False
        print(f"Pegs after = {pegs}")
        return True
    
    def test_replay(self):
        steps = [[0, 1], [0, 2], [1, 2], [0, 1], [2, 0], [2, 1], [0, 1]]
        print(TestHanoi.replay_steps(3, steps))
        return

    def test_all(self):
        return
        for num_rings in range(10):
            result: List[List[int]] = self.solve(num_rings)
            expected_size = TestHanoi.steps_count(num_rings)
            assert len(result) == expected_size, (
                f"Incorrect size expected {expected_size} != {len(result)}")
            assert TestHanoi.replay_steps(result), f"Fail {num_rings} rings"
