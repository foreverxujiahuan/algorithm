from collections import Counter
from typing import List


class Solution:


    def countBadPairs(self, nums: List[int]) -> int:
        nums = [x - i for i, x in enumerate(nums)]
        c = Counter(nums)

        n = len(nums)
        res = n * (n - 1) // 2
        for n in c.values():
            res -= n * (n - 1) // 2

        return res




if __name__ == '__main__':
    solution = Solution()
    nums = [4,1,3,3]
    res = solution.countBadPairs(nums)
    print(res)