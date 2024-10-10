from typing import List
from itertools import accumulate
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = list(accumulate(nums))
        pre_sum = [0] + pre_sum
        num2index = defaultdict(int)
        ans = 0
        for i, n in enumerate(pre_sum):
            target = pre_sum[i] - k
            ans += num2index[target]
            num2index[pre_sum[i]] += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3]
    k = 3
    res = solution.subarraySum(nums, k)
    print(res)