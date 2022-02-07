from typing import (
    List,
)


class Solution:
    """
    @param nums: the input array
    @param target: the target number
    @return: return the target pair
    """
    def twoSumVII(self, nums: List[int], target: int) -> List[List[int]]:
        # write your code here
        nums.sort()
        left = 0
        length = len(nums)
        right = length
        res = []
        while left != right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                res.append([left, right])
                while left+1 < length and nums[left] == nums[left+1]:
                    left += 1
                    res.append([left, right])
                while right-1 >= 0 and nums[right] == nums[right-1]:
                    right -= 1
                    res.append([left, right])
                left += 1
                right -= 1
        return res
