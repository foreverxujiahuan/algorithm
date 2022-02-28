from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [1 for _ in range(length+1)]
        res = 0
        for i in range(length):
            for j in range(i):
                if nums[j] > nums[j-1]:
                    dp[j+1] = dp[j] + 1
                else:
                    dp[j+1] = dp[j]
            res = max(res, dp[i])
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [0,1,0,3,2,3]
    res = solution.lengthOfLIS(nums)
    print(res)
