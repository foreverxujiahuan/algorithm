from typing import List


def rob(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)
    dp = [nums[0], max(nums[0], nums[1])]
    length = len(nums)
    for i in range(2, length):
        dp.append(max(nums[i]+dp[i-2], dp[i-1]))
    return dp[-1]


nums = [2,7,9,3,1]
res = rob(nums)
print(res)
