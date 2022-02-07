from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        cnt = len(prices)
        lengths = []
        cur_length = 1
        for i in range(len(prices)-1):
            if prices[i] - 1 == prices[i + 1]:
                cur_length += 1
            else:
                lengths.append(cur_length)
                cur_length = 1
        if len(prices) >= 2 and prices[-1] == prices[-2] - 1:
            lengths.append(cur_length)
        temp = sum([sum(range(1, length)) for length in lengths if length != 1])
        cnt += temp
        return cnt

solution = Solution()

prices = [12,11,10,9,8,7,6,5,4,3,4,3,10,9,8,7]
res = solution.getDescentPeriods(prices)
print(res)