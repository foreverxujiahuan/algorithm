from itertools import accumulate
from typing import List


class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        conver = [0 for _ in nums]
        conver[0] = nums[0] * 2
        length = len(nums)
        mx = conver[0]
        for i in range(1, length):
            mx = max(mx, nums[i])
            conver[i] = nums[i] + mx
        ans = list(accumulate(conver))
        return ans