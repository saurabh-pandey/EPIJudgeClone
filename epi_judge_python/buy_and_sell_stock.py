from typing import List

from test_framework import generic_test
from tests.test_buy_and_sell_stock import TestBuySellStockOnce


def buy_and_sell_stock_once_v1(prices: List[float]) -> float:
    '''
    O(n^2) time and O(1) space brute-force version
    '''
    sz = len(prices)
    max_profit = 0.0
    for i in range(sz):
        for j in range(i + 1, sz):
            max_profit = max(max_profit, prices[j] - prices[i])
    return max_profit

def crossover_profit(prices: List[float], start, mid, end) -> float:
    if mid <= start:
        return 0.0
    if end <= mid:
        return 0.0
    min_price_left = min(prices[start:mid])
    max_price_right = max(prices[mid:end])
    return max_price_right - min_price_left

def buy_and_sell_stock_once_v2(prices: List[float],
                               start = 0,
                               end = None) -> float:
    '''
    O(nlog(n)) time and O(n) space divide and conquer version
    '''
    if end is None:
        end = len(prices)
    if (end - start) < 2:
        return 0
    mid = (start + end) // 2
    profit_from_left = buy_and_sell_stock_once_v2(prices, start, mid)
    profit_from_right = buy_and_sell_stock_once_v2(prices, mid, end)
    profit_from_crossover = crossover_profit(prices, start, mid, end)
    return max(profit_from_left, profit_from_right, profit_from_crossover)

def buy_and_sell_stock_once(prices: List[float]) -> float:
    # TODO - you fill in here.
    return 0.0


if __name__ == '__main__':
    TestBuySellStockOnce(buy_and_sell_stock_once_v1).run_tests()
    TestBuySellStockOnce(buy_and_sell_stock_once_v2).run_tests()
    # exit(
    #     generic_test.generic_test_main('buy_and_sell_stock.py',
    #                                    'buy_and_sell_stock.tsv',
    #                                    buy_and_sell_stock_once))
