from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            ans = ans ^ n
        return ans


if __name__ == '__main__':
    nums = [2,2,1]
    solution = Solution()
    res = solution.singleNumber(nums)
    print(res)
