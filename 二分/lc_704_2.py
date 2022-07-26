import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        return bisect.bisect_left(nums, target)


if __name__ == '__main__':
    solution = Solution()
    nums = [-1,0,3,5,9,12]
    target = 2
    res = solution.search(nums, target)
    print(res)