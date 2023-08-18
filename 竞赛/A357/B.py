from typing import List


class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        length = len(nums)
        if length == 1:
            return True
        for i in range(length-1):
            if nums[i] + nums[i+1] >= m:
                return True
        return False