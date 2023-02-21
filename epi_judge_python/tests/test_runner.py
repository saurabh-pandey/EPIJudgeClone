test_db = {
    "count_bits": {
        0: 0,
        1: 1,
        2: 1,
        3: 1
    }
}


def run(solution, test_name, verbose=False):
    print(f"Running tests for {test_name}")
    test_data = test_db[test_name]
    for arg, res in test_data.items():
        if verbose:
            print(f"  args = {arg}, expected result = {res}")
        ans = solution(arg)
        if verbose:
            print(f"  actual result = {ans}")
        assert ans == res, f"Expected {res}, actual {ans}"
