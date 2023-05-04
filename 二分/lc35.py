from typing import List
from bisect import bisect_left


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 3, 5, 6]
    target = 5
    res = solution.searchInsert(nums, target)
    print(res)
