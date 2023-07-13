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
            # It is assumed that rings are initially assembled at peg 0
            pegs[0].append(i)
        for step in steps:
            if step:
                from_peg, to_peg = step
                if not pegs[from_peg]:
                    return False
                moved_ring = pegs[from_peg].pop()
                if pegs[to_peg] and not (pegs[to_peg][-1] > moved_ring):
                        return False
                pegs[to_peg].append(moved_ring)
        if pegs[0]:
            # It is assumed to be moved from peg 0
            return False
        filled_peg, empty_peg = pegs[1], pegs[2]
        if not filled_peg:
            filled_peg, empty_peg = empty_peg, filled_peg
        if len(filled_peg) != num_rings:
            return False
        if any(filled_peg[i] <= filled_peg[i + 1]
               for i in range(num_rings - 1)):
            return False
        return True
    
    def test_replay_0_ring(self):
        num_rings = 0
        steps = [[]]
        assert TestHanoi.replay_steps(num_rings, steps), (
            f"Failed replay {num_rings} rings")
        steps = [[0, 1]]
        assert TestHanoi.replay_steps(num_rings, steps) == False, (
            f"Failed replay {num_rings} rings")
    
    def test_replay_1_ring(self):
        num_rings = 1
        steps = [[0, 1]]
        assert TestHanoi.replay_steps(num_rings, steps), (
            f"Failed replay {num_rings} rings")
        steps = [[0, 2]]
        assert TestHanoi.replay_steps(num_rings, steps), (
            f"Failed replay {num_rings} rings")
        steps = [[1, 0]]
        assert TestHanoi.replay_steps(num_rings, steps) == False, (
            f"Failed replay {num_rings} rings")
        steps = [[]]
        assert TestHanoi.replay_steps(num_rings, steps) == False, (
            f"Failed replay {num_rings} rings")
    
    def test_replay_2_ring(self):
        num_rings = 2
        steps = [[0, 2], [0, 1], [2, 1]]
        assert TestHanoi.replay_steps(num_rings, steps), (
            f"Failed replay {num_rings} rings")
        steps = [[0, 1], [0, 2], [1, 2]]
        assert TestHanoi.replay_steps(num_rings, steps), (
            f"Failed replay {num_rings} rings")
        steps = [[0, 2], [0, 1]]
        assert TestHanoi.replay_steps(num_rings, steps) == False, (
            f"Failed replay {num_rings} rings")
        steps = [[0, 2]]
        assert TestHanoi.replay_steps(num_rings, steps) == False, (
            f"Failed replay {num_rings} rings")
        steps = [[]]
        assert TestHanoi.replay_steps(num_rings, steps) == False, (
            f"Failed replay {num_rings} rings")

    def test_replay_3_ring(self):
        num_rings = 3
        steps = [[0, 1], [0, 2], [1, 2], [0, 1], [2, 0], [2, 1], [0, 1]]
        assert TestHanoi.replay_steps(num_rings, steps), (
            f"Failed replay {num_rings} rings")
        steps = [[0, 2], [0, 1], [2, 1], [0, 2], [1, 0], [1, 2], [0, 2]]
        assert TestHanoi.replay_steps(num_rings, steps), (
            f"Failed replay {num_rings} rings")
        steps = [[0, 1], [0, 2], [1, 2], [0, 1], [2, 0], [2, 1], [0, 2]]
        assert TestHanoi.replay_steps(num_rings, steps) == False, (
            f"Failed replay {num_rings} rings")
        steps = [[0, 1], [0, 2], [1, 2], [0, 1], [2, 0], [2, 1]]
        assert TestHanoi.replay_steps(num_rings, steps) == False, (
            f"Failed replay {num_rings} rings")
        steps = [[0, 2], [1, 2], [0, 1], [2, 0], [2, 1], [0, 1]]
        assert TestHanoi.replay_steps(num_rings, steps) == False, (
            f"Failed replay {num_rings} rings")
        steps = [[0, 1], [0, 2], [0, 1], [2, 0], [2, 1], [0, 1]]
        assert TestHanoi.replay_steps(num_rings, steps) == False, (
            f"Failed replay {num_rings} rings")
        steps = [[0, 1], [0, 2], [1, 2], [0, 1], [2, 1], [2, 1], [0, 1]]
        assert TestHanoi.replay_steps(num_rings, steps) == False, (
            f"Failed replay {num_rings} rings")
        steps = [[0, 1], [0, 1], [0, 1]]
        assert TestHanoi.replay_steps(num_rings, steps) == False, (
            f"Failed replay {num_rings} rings")
        steps = [[0, 1], [0, 2]]
        assert TestHanoi.replay_steps(num_rings, steps) == False, (
            f"Failed replay {num_rings} rings")
        steps = [[0, 1]]
        assert TestHanoi.replay_steps(num_rings, steps) == False, (
            f"Failed replay {num_rings} rings")
        steps = [[]]
        assert TestHanoi.replay_steps(num_rings, steps) == False, (
            f"Failed replay {num_rings} rings")

    def test_all(self):
        return
        for num_rings in range(10):
            result: List[List[int]] = self.solve(num_rings)
            expected_size = TestHanoi.steps_count(num_rings)
            assert len(result) == expected_size, (
                f"Incorrect size expected {expected_size} != {len(result)}")
            assert TestHanoi.replay_steps(result), f"Fail {num_rings} rings"
