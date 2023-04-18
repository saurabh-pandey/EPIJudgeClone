from test_framework import generic_test

from tests.test_evaluate_rpn import TestEvaluateRPN


def evaluate_v1(expression: str) -> int:
    '''
    My O(n) space and O(n) time version where n is length of string
    '''
    pass

def evaluate(expression: str) -> int:
    # TODO - you fill in here.
    return 0


if __name__ == '__main__':
    TestEvaluateRPN(evaluate_v1).run_tests()
    # exit(
    #     generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
    #                                    evaluate))
