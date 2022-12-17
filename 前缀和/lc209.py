from typing import List
import bisect


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_sum = [0]
        for i, n in enumerate(nums):
            t = prefix_sum[-1] + n
            prefix_sum.append(t)
        length = len(prefix_sum)
        res = 999999
        flag = 0
        for i in range(length):
            j = bisect.bisect_left(prefix_sum, target + prefix_sum[i], lo=i+1, hi=length)
            if j < length:
                res = min(j-i, res)
                flag = 1
        if flag:
            return res
        return 0


if __name__ == '__main__':
    target = 7
    nums = [2,3,1,2,4,3]
    solution = Solution()
    res = solution.minSubArrayLen(target, nums)
    print(res)
