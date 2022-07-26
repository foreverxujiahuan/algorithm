from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            dp.append(max(nums[i], dp[i-1] + nums[i]))
        return max(dp)

if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solution = Solution()
    res = solution.maxSubArray(nums)
    print(res)