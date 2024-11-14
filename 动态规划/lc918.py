from typing import List
from itertools import accumulate


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        dp = [0 for _ in nums]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        pre_sum = list(accumulate(nums))
        max_pre_sum = [-99999 for _ in pre_sum]
        max_pre_sum[0] = pre_sum[0]
        for i in range(1, len(pre_sum)):
            max_pre_sum[i] = max(pre_sum[i], max_pre_sum[i-1])
        mx = -9999999
        for i in range(1, len(nums)):
            cur_post_sum = pre_sum[-1] - pre_sum[i]
            cur_pre_sum = max_pre_sum[i-1]
            mx = max(mx, cur_post_sum + cur_pre_sum)
        return max(mx, max(dp))

if __name__ == '__main__':
    solution = Solution()
    nums = [3,-2,2,-3]
    res = solution.maxSubarraySumCircular(nums)
    print(res)