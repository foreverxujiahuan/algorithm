from typing import List
from itertools import accumulate



class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        pre_sum = list(accumulate(nums))
        print(pre_sum)
        ans = len([t > 0 for t in pre_sum])
        return ans


if __name__ == '__main__':
    nums = [2,-1,0,1,-3,3,-3]
    solution = Solution()
    res = solution.maxScore(nums)
    print(res)