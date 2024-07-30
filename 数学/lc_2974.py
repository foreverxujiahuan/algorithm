from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        ans = []
        length = len(nums)
        mid = length // 2
        nums.sort()
        for i in range(mid):
            ans.append(nums[2*i+1])
            ans.append(nums[2*i])
        return ans
