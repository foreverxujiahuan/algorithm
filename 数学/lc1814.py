from collections import defaultdict
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for i, n in enumerate(nums):
            d[nums[i] - self.rev(nums[i])] += 1
        ans = 0
        for v in d.values():
            ans += sum(range(v))
        return ans

    def rev(self, n):
        return int(str(n)[::-1])


if __name__ == '__main__':
    solution = Solution()
    nums = [13,10,35,24,76]
    res = solution.countNicePairs(nums)
    print(res)