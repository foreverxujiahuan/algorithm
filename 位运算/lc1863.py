from functools import reduce
from operator import xor
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        l = len(nums)
        for i in range(l):
            for j in range(i+1, l+1):
                cur = nums[i: j]
                ans += reduce(xor, cur)

        return ans


if __name__ == '__main__':
    nums = [5 ,1, 6]
    solution = Solution()
    res = solution.subsetXORSum(nums)
    print(res)