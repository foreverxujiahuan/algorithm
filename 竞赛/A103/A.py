from typing import List


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        ans = sum(range(mx, mx+k))
        return ans