from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        tmp = []
        mi, mx = max(nums), min(nums)
        for n in nums:
            if n == mi or n == mx:
                continue
            tmp.append(n)
        if tmp:
            return max(tmp)
        return -1