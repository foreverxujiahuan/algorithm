import math
from typing import List


def maxProfit(prices: List[int]) -> int:
    min_price = math.pow(2, 31)
    max_value = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_value:
            max_value = price - min_price
    return max_value


prices = [7,1,5,3,6,4]
res = maxProfit(prices)
print(res)
