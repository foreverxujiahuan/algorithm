import bisect
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans1 = bisect.bisect_left(nums, target)
        ans2 = bisect.bisect_right(nums, target) - 1
        if ans1 < 0 or ans1 >= len(nums):
            return [-1, -1]
        if nums[ans1] != target:
            return [-1, -1]
        return [ans1, ans2]

if __name__ == '__main__':
    nums = [2, 2]
    target = 3
    solution = Solution()
    res = solution.searchRange(nums, target)
    print(res)
