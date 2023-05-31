from typing import List

from test_framework import generic_test, test_utils

from tests.test_anagrams import TestAnagrams


def find_anagrams_v1(dictionary: List[str]) -> List[List[str]]:
    '''
    My attempt
    '''
    word_dist_repo = []
    anagrams = []
    for word in dictionary:
        word_dist = {}
        for l in word:
            if l in word_dist:
                word_dist[l] += 1
            else:
                word_dist[l] = 1
        if word_dist in word_dist_repo:
            index = word_dist_repo.index(word_dist)
            if index < len(anagrams):
                anagrams[index].append(word)
            else:
                print("Should not happen")
                anagrams.append([word])
        else:
            word_dist_repo.append(word_dist)
            anagrams.append([word])
    anagrams[:] = [a for a in anagrams if len(a) > 1]
    return anagrams


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    # TODO - you fill in here.
    return []


if __name__ == '__main__':
    TestAnagrams(find_anagrams_v1).run_tests()
    # exit(
    #     generic_test.generic_test_main(
    #         'anagrams.py',
    #         'anagrams.tsv',
    #         find_anagrams,
    #         comparator=test_utils.unordered_compare))
