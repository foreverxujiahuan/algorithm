from typing import List


def maxSubArray(nums: List[int]) -> int:
    length = len(nums)
    dp = [nums[0]]
    for i in range(1, length):
        dp.append(max(nums[i], dp[i-1] + nums[i]))
    return max(dp)


nums = [-100000]
res = maxSubArray(nums)
print(res)
