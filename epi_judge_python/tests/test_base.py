import traceback

from typing import Callable

from test_framework.test_failure import TestFailure


class TestBase:
    def __init__(self, solve: Callable[[], None] = None,
                 message: str = None) -> None:
        self.solve = solve
        self.message = (
            message if message else solve.__name__ if solve else "None")

    def run_tests(self, pattern: str = None, verbose: bool = False) -> None:
        print("Testing", self.message)
        if not pattern:
            pattern = "test_"
        failed_tests = {}
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
                        failed_tests[func_name] = err
                        if verbose:
                            print(f" Failed {func_name}")
                        else:
                            print("F", end="")
                    except TestFailure as err:
                        failed_tests[func_name] = err.get_description()
                        if verbose:
                            print(f" Failed {func_name}")
                        else:
                            print("F", end="")
                    except Exception as err:
                        print(f"Exception class ={type(err)}, err = {err}")
                        failed_tests[func_name] = err
                        if verbose:
                            print(f" Failed {func_name}")
                        else:
                            print("F", end="")
                        print("\nTraceback:")
                        print(traceback.format_exc())
        print()
        if failed_tests:
            print("Summary of test failure (test name => error message):")
            for t, e in failed_tests.items():
                print(f" - {t} => {e}")
        else:
            print("All tests passed")
