from typing import List
import math


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        visited = set()
        nums.sort()
        valid = set(nums)
        mx = -1
        for n in nums:
            cnt = 1
            if n in visited:
                continue
            cur = n
            while cur ** 2 in valid:
                cnt += 1
                cur = cur ** 2
            if cnt == 1:
                continue
            mx = max(cnt, mx)
        return mx


if __name__ == '__main__':
    nums = [2,3,5,6,7]
    solution = Solution()
    res = solution.longestSquareStreak(nums)
    print(res)
