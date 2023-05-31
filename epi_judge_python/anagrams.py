from typing import Dict, List

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


# def find_anagrams_v2(dictionary: List[str]) -> List[List[str]]:
#     '''
#     My attempt
#     '''
#     def hash_word_distrib(word_distrib: Dict[str, int]) -> str:
#         hash_value = []
#         for c, v in word_distrib.items():
#             hash_value.append(c)
#             hash_value.append(str(v))
#         return "".join(hash_value)
#     word_dist_repo = {}
#     anagrams = {}
#     for word in dictionary:
#         word_dist = {l: 0 for l in word}
#         for l in word:
#                 word_dist[l] += 1
#         hashed_val = hash_word_distrib(word_dist)
#         if hashed_val in word_dist_repo:
#             index = word_dist_repo.index(word_dist)
#             if index < len(anagrams):
#                 anagrams[index].append(word)
#             else:
#                 print("Should not happen")
#                 anagrams.append([word])
#         else:
#             word_dist_repo.append(word_dist)
#             anagrams.append([word])
#     anagrams[:] = [a for a in anagrams if len(a) > 1]
#     return anagrams



def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    return find_anagrams_v1(dictionary)


if __name__ == '__main__':
    TestAnagrams(find_anagrams_v1).run_tests()
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
