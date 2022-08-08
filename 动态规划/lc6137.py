from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        f = [True] + [False] * n
        for i, x in enumerate(nums):
            if i > 0 and f[i - 1] and x == nums[i - 1] or \
                    i > 1 and f[i - 2] and (x == nums[i - 1] == nums[i - 2] or
                                            x == nums[i - 1] + 1 == nums[i - 2] + 2):
                f[i + 1] = True
        return f[n]


