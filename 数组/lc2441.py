from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        arr_set = set(nums)
        valid_nums = []
        for n in nums:
            if -n in arr_set:
                valid_nums.append(n)
        return max(valid_nums) if valid_nums else -1
