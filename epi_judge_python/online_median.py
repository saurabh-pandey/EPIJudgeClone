import heapq

from typing import Iterator, List

from test_framework import generic_test

from tests.test_online_median import TestOnlineMedian

def online_median_v1(sequence: Iterator[int]) -> List[float]:
    '''
    My attempt with O(nlog(n)) for n entries
    '''
    min_heap = []
    max_heap = []
    medians = []
    for value in sequence:
        assert len(max_heap) >= len(min_heap), (
            "Max heap is always bigger or equal")
        assert len(max_heap) - len(min_heap) <= 1, "Length invariant failed"
        if not max_heap:
            heapq.heappush(max_heap, -value)
        elif not min_heap:
            if value > -max_heap[0]:
                heapq.heappush(min_heap, value)
            else:
                max_val = -heapq.heapreplace(max_heap, -value)
                heapq.heappush(min_heap, max_val)
        else:
            if value <= -max_heap[0]:
                if len(max_heap) == len(min_heap):
                    heapq.heappush(max_heap, -value)
                else:
                    max_val = -heapq.heapreplace(max_heap, -value)
                    heapq.heappush(min_heap, max_val)
            elif value >= min_heap[0]:
                if len(max_heap) == len(min_heap):
                    min_val = heapq.heapreplace(min_heap, value)
                    heapq.heappush(max_heap, -min_val)
                else:
                    heapq.heappush(min_heap, value)
            else:
                if len(max_heap) == len(min_heap):
                    heapq.heappush(max_heap, -value)
                else:
                    heapq.heappush(min_heap, value)
        if len(max_heap) == len(min_heap):
            medians.append((-max_heap[0] + min_heap[0])/2)
        else:
            medians.append(-max_heap[0])
    return medians


def online_median_v2(sequence: Iterator[int]) -> List[float]:
    '''
    Code wise better version with flipped conditional checking with same runtime
    '''
    max_heap = []
    min_heap = []
    medians = []
    for value in sequence:
        if len(max_heap) == len(min_heap):
            if not min_heap or value <= min_heap[0]:
                heapq.heappush(max_heap, -value)
            else:
                min_val = heapq.heapreplace(min_heap, value)
                heapq.heappush(max_heap, -min_val)
            medians.append(-max_heap[0])
        else:
            if value >= -max_heap[0]:
                heapq.heappush(min_heap, value)
            else:
                max_val = -heapq.heapreplace(max_heap, -value)
                heapq.heappush(min_heap, max_val)
            medians.append((min_heap[0] - max_heap[0])/2)
    return medians


def online_median(sequence: Iterator[int]) -> List[float]:
    # return online_median_v1(sequence)
    return online_median_v2(sequence)


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    TestOnlineMedian(online_median_v1).run_tests()
    TestOnlineMedian(online_median_v2).run_tests()
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
