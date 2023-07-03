from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        a, b = prices[0], prices[1]
        if money >= a + b:
            return money - a - b
        return money

