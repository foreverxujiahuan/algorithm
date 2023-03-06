from typing import List


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        ans = []
        length = len(nums)
        for i in range(length):
            ans.append(abs(sum(nums[:i]) - sum(nums[i+1:])))
        return ans
