from bisect import bisect_left, bisect_right
from itertools import accumulate
from typing import List


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        length = len(nums)
        mod = 10**9 + 7
        pre_sum = list(accumulate(nums))
        ans = 0
        for i in range(length-2):
            p = bisect_left(pre_sum, 2 * pre_sum[i], i+1, length-1)
            q = bisect_right(pre_sum, (pre_sum[i] + pre_sum[-1]) / 2, p, length-1)
            ans += q - p
        return ans % mod


if __name__ == '__main__':
    nums = [1,1,1]
    solution = Solution()
    res = solution.waysToSplit(nums)
    print(res)