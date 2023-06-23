from tests.test_base import TestBase


class TestIntervalUnion(TestBase):
    # Intervals are passed as mathematical intervals where () means open and
    # [] means closed
    def test_example1(self):
        # a = [((False, 3), (False, 5)), ((False, 7), (True, 9)),
        #      ((True, 6), (True, 7)), ((False, 1), (False, 2)),
        #      ((True, 7), (True, 11)), ((True, 2), (True, 2)),
        #      ((False, 3), (False, 5)), ((True, 11), (True, 15)),
        #      ((False, 4), (True, 6)), ((False, 15), (False, 16)),
        #      ((True, 8), (True, 13)), ((False, 4), (False, 6)),
        #      ((False, 1), (True, 2)), ((False, 2), (True, 2))]
        # a.sort(key=lambda i: (i[0][1], i[0][0], i[1][1], i[1][0]))
        # print(a)
        # return
        intervals = ["(0, 3)", "[1, 1]", "[2, 4]", "[3, 4)", "[5, 7)",
                     "[7, 8)", "[8, 11)", "(9, 11]", "[12, 14]", "(12, 16]",
                     "(13, 15)", "(16, 17)"]
        self.solve(intervals)
        # result = self.solve(intervals)
        # expected = ["(0, 4]", "[5, 11]", "[12, 17)"]
        # assert result == expected, f"Expected {expected} != {result} result"
