from typing import Callable

class TestBase:
    def __init__(self, solve: Callable[[], None], message: str = None) -> None:
        # print("Type of solve = ", type(solve), ", name = ", solve.__name__)
        # print("Dir solve = ", dir(solve))
        # print("Repr solve = ", repr(solve))
        self.solve = solve
        self.message = message if message else solve.__name__

    def run_tests(self, verbose: bool = False) -> None:
        # print("Base Self = ", self)
        print("Running", self.message)
        # method_list = [func for func in dir(self) if callable(getattr(self, func)) and func.startswith("test_")]
        # print(method_list)
        for func_name in dir(self):
            if func_name.startswith("test_"):
                func = getattr(self, func_name)
                if callable(func):
                    if verbose:
                        print(f" Calling {func_name}")
                    try:
                        func()
                    except:
                        print(f" Failed {func_name}")

