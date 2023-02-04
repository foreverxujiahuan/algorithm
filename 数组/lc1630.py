from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for li, ri in zip(l, r):
            ans.append(self.f(nums[li: ri + 1]))
        return ans

    def f(self, nums):
        length = len(nums)
        if length < 2:
            return False
        nums.sort()
        target = nums[1] - nums[0]
        for i in range(1, length):
            if nums[i] - nums[i-1] != target:
                return False
        return True

