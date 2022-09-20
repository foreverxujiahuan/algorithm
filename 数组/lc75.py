from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i, n in enumerate(nums):
            if n == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        for i, n in enumerate(nums):
            if n == 1:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1