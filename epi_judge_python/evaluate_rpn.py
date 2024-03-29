from test_framework import generic_test

from tests.test_evaluate_rpn import TestEvaluateRPN


def evaluate_v1(expression: str) -> int:
    '''
    My O(n) space and O(n) time version where n is length of string
    '''
    def eval(s, stack):
        if s in ("+", "-", "*", "/"):
            num2 = stack.pop()
            num1 = stack.pop()
            if s == "+":
                stack.append(num1 + num2)
            elif s == "-":
                stack.append(num1 - num2)
            elif s == "*":
                stack.append(num1 * num2)
            elif s == "/":
                assert num2 != 0
                stack.append(num1 // num2)
        else:
            stack.append(int(s))
    eval_stack = []
    sub_str = ""
    for s in expression:
        if s == ",":
            eval(sub_str, eval_stack)
            sub_str = ""
        else:
            sub_str += s
    eval(sub_str, eval_stack)
    return eval_stack[0]


def evaluate_v2(expression: str) -> int:
    '''
    Book's version
    '''
    delimiter = ","
    operators = {'+': lambda y, x: x + y, '-': lambda y, x: x - y,
                 '*': lambda y, x: x * y, '/': lambda y, x: x // y}
    intermediate_results = []
    for token in expression.split(delimiter):
        if token in operators:
            intermediate_results.append(operators[token](
                intermediate_results.pop(), intermediate_results.pop()
            ))
        else:
            intermediate_results.append(int(token))
    return intermediate_results[-1]


def evaluate(expression: str) -> int:
    # return evaluate_v1(expression)
    return evaluate_v2(expression)


if __name__ == '__main__':
    TestEvaluateRPN(evaluate_v1).run_tests()
    TestEvaluateRPN(evaluate_v2).run_tests()
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
