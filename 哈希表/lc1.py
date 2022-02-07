from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2index = dict()
        for i in range(len(nums)):
            nums2index[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in nums2index.keys() and nums2index[target - nums[i]] != i:
                return [i, nums2index[target - nums[i]]]
        return []
