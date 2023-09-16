from collections import Counter
from typing import List


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        counter = Counter(nums)
        mx = max(counter.values())
        mi = 0
        if len(nums) % 2 == 1:
            mi = 1
        ans = max(mi, mx - (sum(counter.values()) - mx))
        return ans


if __name__ == '__main__':
    nums = [2]
    solution = Solution()
    res = solution.minLengthAfterRemovals(nums)
    print(res)