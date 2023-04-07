from test_framework import generic_test
from tests.test_look_and_say import TestLookAndSay


def look_and_say_v1(n: int) -> str:
    '''
    My version
    '''
    digits = ["1"]
    for _ in range(2, n + 1):
        running_digit = digits[0]
        count = 0
        next_digits = []
        for i in range(0, len(digits)):
            if running_digit == digits[i]:
                count += 1
            else:
                next_digits.append(str(count))
                next_digits.append(running_digit)
                running_digit = digits[i]
                count = 1
        next_digits.append(str(count))
        next_digits.append(running_digit)
        digits = next_digits[:]
    return "".join(digits)


def look_and_say(n: int) -> str:
    return look_and_say_v1(n)


if __name__ == '__main__':
    TestLookAndSay(look_and_say_v1).run_tests()
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
