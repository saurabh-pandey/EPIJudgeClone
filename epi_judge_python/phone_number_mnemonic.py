from typing import List

from test_framework import generic_test, test_utils

from tests.test_phone_number_mnemonic import TestPhoneNumberMnemonic


def phone_mnemonic_v1(phone_number: str) -> List[str]:
    '''
    My version with O(n*4^n) time complexity
    '''
    def phone_mnemonic_recursive(i: int) -> None:
        if i == len(phone_number):
            result.append("".join(word))
        else:
            num = int(phone_number[i])
            for c in TestPhoneNumberMnemonic.PHONE_NUM_CHAR_MAP[num]:
                word.append(c)
                phone_mnemonic_recursive(i + 1)
                word.pop()
    result = []
    word = []
    phone_mnemonic_recursive(0)
    return result


def phone_mnemonic_v2(phone_number: str) -> List[str]:
    '''
    Book's version with same time complexity
    '''
    def phone_mnemonic_recursive(i: int) -> None:
        if i == len(phone_number):
            result.append("".join(word))
        else:
            num = int(phone_number[i])
            for c in TestPhoneNumberMnemonic.PHONE_NUM_CHAR_MAP[num]:
                word[i] = c
                phone_mnemonic_recursive(i + 1)
    result = []
    word = ['0'] * len(phone_number)
    phone_mnemonic_recursive(0)
    return result


def phone_mnemonic(phone_number: str) -> List[str]:
    # return phone_mnemonic_v1(phone_number)
    return phone_mnemonic_v2(phone_number)


if __name__ == '__main__':
    TestPhoneNumberMnemonic(phone_mnemonic_v1).run_tests()
    TestPhoneNumberMnemonic(phone_mnemonic_v2).run_tests()
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
