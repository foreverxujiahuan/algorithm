from functools import reduce
from itertools import permutations
from typing import List


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        cur = reduce(lambda x, y: x * y, nums)
        if cur > 0:
            return cur
        if cur < 0:
            tmp = [t for t in nums if t < 0]
            if len(tmp) == 1:
                return tmp[0]
            mx = max(tmp)
            return int(cur / mx)
        if cur == 0:
            if nums.count(0) == len(nums):
                return 0
            else:
                nums = [n for n in nums if n != 0]
                cur = reduce(lambda x, y: x * y, nums)
                if cur > 0:
                    return cur
                if cur < 0:
                    tmp1 = [t for t in nums if t < 0]
                    tmp2 = [t for t in nums if t > 0]
                    mx = max(tmp1)
                    if len(tmp1) == 1:
                        return 0
                    return int(cur / mx)



if __name__ == '__main__':
    solution = Solution()
    nums = [2,2,7,0,-4,9,4]
    res = solution.maxStrength(nums)
    print(res)