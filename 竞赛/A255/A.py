import math
from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        max_num = max(nums)
        min_num = min(nums)
        return self.f(max_num, min_num)


    def f(self, max_num, min_num):
        for i in range(min_num):
            t = min_num - i
            if max_num % t == 0 and min_num % t == 0:
                return t

if __name__ == '__main__':
    nums = [3,3]
    s = Solution()
    res = s.findGCD(nums)
    print(res)