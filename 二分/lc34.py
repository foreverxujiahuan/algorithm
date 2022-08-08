import bisect
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        ans1 = bisect.bisect_left(nums, target)
        ans2 = bisect.bisect_right(nums, target) - 1
        return [ans1, ans2]

if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    solution = Solution()
    res = solution.searchRange(nums, target)
    print(res)
