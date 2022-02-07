from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_sum = [0]
        for num in nums:
            temp = num + prefix_sum[-1]
            prefix_sum.append(temp)
