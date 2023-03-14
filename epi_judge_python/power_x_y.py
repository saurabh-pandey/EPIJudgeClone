from test_framework import generic_test
from tests.test_power_x_y import TestPowerXY

def power_v1(x: float, y: int) -> float:
    '''
    O(n) recursive version
    '''
    if x == 0.0:
        return 0.0
    if y == 0:
        return 1.0
    if y < 0:
        x, y = 1.0/x, -y
    x_power_half = power_v1(x, y >> 1)
    if y & 1:
        return x * x_power_half * x_power_half
    else:
        return x_power_half * x_power_half

def power_v2(x: float, y: int) -> float:
    '''
    Books O(n) loop version
    '''
    result, power = 1.0, y
    if y < 0:
        x, power = 1.0/x, -power
    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1
    return result

def power(x: float, y: int) -> float:
    # return power_v1(x, y)
    return power_v2(x, y)


if __name__ == '__main__':
    TestPowerXY(power_v1).run_tests()
    TestPowerXY(power_v2).run_tests()
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
