from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        num2cnt = Counter(nums)
        max_value = max(nums)
        nums = [0] * (max_value + 1)
        for n, cnt in num2cnt.items():
            nums[n] = cnt
        dp = [0, 1 * nums[1]]
        for i in range(2, max_value + 1):
            t = max(dp[i-1], dp[i-2] + nums[i] * i)
            dp.append(t)
        return max(dp)


if __name__ == '__main__':
    nums = [2,2,3,3,3,4]
    solution = Solution()
    res = solution.deleteAndEarn(nums)
    print(res)