from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0]
        for i in range(n):
            prefix_sum.append(nums[i] + prefix_sum[-1])
        for i in range(1, n+1):
            if prefix_sum[i-1] == prefix_sum[-1] - prefix_sum[i]:
                return i-1
        return -1
