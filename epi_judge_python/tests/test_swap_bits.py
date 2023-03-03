from tests.test_base import TestBase

class TestSwapBits(TestBase):
    # def __init__(self, solve) -> None:
    #     super(solve)

    # def run_tests(self) -> None:
    #     method_list = [func for func in dir(self) if callable(getattr(self, func)) and func.startswith("test_")]
    #     print(method_list)

    def test_example1(self) -> None:
        # print("Test Self = ", self)
        x = 2
        i = 0
        j = 1
        expected = 3
        assert self.solve(x, i, j) == expected

    def test_example2(self) -> None:
        # print("None")
        x = 1
        i = 0
        j = 1
        expected = 3
        assert self.solve(x, i, j) == expected