from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        mid = len(nums) // 2
        ave = []
        for i in range(mid):
            mi, mx = nums[i], nums[-i-1]
            ave.append((mi+mx) / 2)
        return min(ave)
