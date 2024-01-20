from collections import Counter
from typing import List
from math import ceil, gcd


class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        g = 0
        for num in nums:
            g = gcd(g, num)
        return max(1, ceil(nums.count(g) / 2))


if __name__ == '__main__':
    # nums = [4,4,4] # 2
    # nums = [2,2,4,4,2,1] # 1
    # nums = [3,4,3,4,1,1,1,2] # 2
    # nums = [5,5,5,10,5] # 2
    nums = [2,2,2,5,9,10]
    # nums = [1]
    solution = Solution()
    res = solution.minimumArrayLength(nums)
    print(res)