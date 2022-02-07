from typing import (
    List,
)

class Solution:
    """
    @param nums: a list of integer
    @param target: an integer
    @return: nothing
    """
    def MoveTarget(self, nums: List[int], target: int):
        # write your code here
        left, right = len(nums) - 1, len(nums) - 1
        count = 0
        while left >= 0:
            if nums[left] != target:
                nums[right] = nums[left]
                right -= 1
            else:
                count += 1
            left -= 1
        for i in range(count):
            nums[i] = target
        # for i, n in enumerate(nums):
        #     if n == target:
        #         nums[i], nums[index] = nums[index], nums[i]
        #         index += 1
