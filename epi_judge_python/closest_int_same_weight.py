from test_framework import generic_test

def closest_int_same_bit_count_v1(x: int) -> int:
    '''
    Brute-force version
    '''
    diff = 1
    while True:
        if x > diff:
            new_x = x - diff


def closest_int_same_bit_count(x: int) -> int:
    # TODO - you fill in here.
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
