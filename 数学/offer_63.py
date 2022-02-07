from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min_list = []
        cur_min = float('inf')
        for n in prices:
            if n < cur_min:
                cur_min_list.append(n)
                cur_min = n
            else:
                cur_min_list.append(cur_min)
        res = 0
        for n, min_value in zip(prices, cur_min_list):
            if n - min_value > res:
                res = n - min_value
        return res