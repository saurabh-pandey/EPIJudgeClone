from typing import List

from test_framework import generic_test, test_utils

from tests.test_phone_number_mnemonic import TestPhoneNumberMnemonic


def phone_mnemonic_v1(phone_number: str) -> List[str]:
    '''
    My version
    '''
    return []


def phone_mnemonic(phone_number: str) -> List[str]:
    # TODO - you fill in here.
    return []


if __name__ == '__main__':
    TestPhoneNumberMnemonic(phone_mnemonic_v1).run_tests()
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
