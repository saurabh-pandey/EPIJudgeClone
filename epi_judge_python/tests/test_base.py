from typing import Callable

class TestBase:
    def __init__(self, solve: Callable[[], None], message: str = None) -> None:
        self.solve = solve
        self.message = message if message else solve.__name__

    def run_tests(self, pattern: str = None, verbose: bool = False) -> None:
        print("Testing", self.message)
        if not pattern:
            pattern = "test_"
        failed_tests = []
        for func_name in dir(self):
            if func_name.startswith(pattern):
                func = getattr(self, func_name)
                if callable(func):
                    if verbose:
                        print(f" Calling {func_name}")
                    try:
                        func()
                        if not verbose:
                            print(".", end="")
                    except AssertionError as err:
                        failed_tests.append(func_name)
                        if verbose:
                            print(f" Failed {func_name}")
                        else:
                            print("F", end="")
                    except Exception as err:
                        print(f"Exception class ={type(err)}")
                        failed_tests.append(func_name)
                        if verbose:
                            print(f" Failed {func_name}")
                        else:
                            print("F", end="")
        print()
        if failed_tests:
            print("Following tests failed:")
            for t in failed_tests:
                print(f"  - {t}")
        else:
            print("All tests passed")
