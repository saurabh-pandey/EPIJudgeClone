import functools
import heapq
import itertools
import math
from typing import Iterator, List, Tuple

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

from tests.test_k_closest_stars import TestKClosestStars


class Star:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs: 'Star') -> bool:
        return self.distance < rhs.distance

    def __repr__(self):
        return str(self.distance)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, rhs):
        return math.isclose(self.distance, rhs.distance)


def find_closest_k_stars_v1(stars: Iterator[Star], k: int) -> List[Star]:
    '''
    My O(nlog(k)) version
    '''
    max_heap = []
    for star in itertools.islice(stars, k):
        heapq.heappush(max_heap, (-star.distance, star))
    for star in stars:
        max_so_far = -max_heap[0][0]
        if star.distance < max_so_far:
            heapq.heapreplace(max_heap, (-star.distance, star))
    return [s[1] for s in heapq.nsmallest(k, max_heap)]


def find_closest_k_stars_v2(stars: Iterator[Star], k: int) -> List[Star]:
    '''
    Book's more succinct O(nlog(k)) version
    '''
    max_heap = []
    for star in stars:
        heapq.heappush(max_heap, (-star.distance, star))
        if len(max_heap) == k + 1:
            heapq.heappop(max_heap)
    return [s[1] for s in heapq.nsmallest(k, max_heap)]


def find_closest_k_stars(stars: Iterator[Star], k: int) -> List[Star]:
    # return find_closest_k_stars_v1(stars, k)
    return find_closest_k_stars_v2(stars, k)


def comp(expected_output, output):
    if len(output) != len(expected_output):
        return False
    return all(
        math.isclose(s.distance, d)
        for s, d in zip(sorted(output), expected_output))


@enable_executor_hook
def find_closest_k_stars_wrapper(executor, stars, k):
    stars = [Star(*a) for a in stars]
    return executor.run(functools.partial(find_closest_k_stars, iter(stars),
                                          k))


def calling_wrapper_v1(coords: List[Tuple[float, float, float]],
                       k: int) -> List[Tuple[float, float, float]]:
    stars = [Star(c[0], c[1], c[2]) for c in coords]
    result = find_closest_k_stars_v1(iter(stars), k)
    return [(s.x, s.y, s.z) for s in result]


def calling_wrapper_v2(coords: List[Tuple[float, float, float]],
                       k: int) -> List[Tuple[float, float, float]]:
    stars = [Star(c[0], c[1], c[2]) for c in coords]
    result = find_closest_k_stars_v2(iter(stars), k)
    return [(s.x, s.y, s.z) for s in result]


if __name__ == '__main__':
    TestKClosestStars(calling_wrapper_v1).run_tests()
    TestKClosestStars(calling_wrapper_v2).run_tests()
    exit(
        generic_test.generic_test_main('k_closest_stars.py',
                                       'k_closest_stars.tsv',
                                       find_closest_k_stars_wrapper, comp))
