from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(1, i):
                if nums[j] - nums[j-1] <= k:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

