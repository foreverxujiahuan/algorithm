from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        d = dict()
        for i in range(len(nums) - 1):
            t = sum(nums[i: i+2])
            d[t] = d.get(t, 0) + 1
        return max(d.values()) >= 2
