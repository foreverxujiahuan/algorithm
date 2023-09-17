from collections import Counter
from typing import List


class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n + 1):
            if i and nums[i - 1] >= i:  # 不能选
                continue
            if n > i >= nums[i]: 
                continue
            ans += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    # nums = [6,0,3,3,6,7,2,7] #3
    nums = [0,1,5,6,8,7,4,7,2]
    res = solution.countWays(nums)
    print(res)