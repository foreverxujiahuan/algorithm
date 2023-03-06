from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for i, n in enumerate(nums):
            target1 = lower - n
            target2 = upper - n
            l = bisect_left(nums, target1, 0, i)
            r = bisect_right(nums, target2, 0, i)
            ans += r - l
        return ans

if __name__ == '__main__':
    nums = [0, 1, 7, 4, 4, 5]
    lower = 3
    upper = 6
    solution = Solution()
    res = solution.countFairPairs(nums, lower, upper)
    print(res)
