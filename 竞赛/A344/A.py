from typing import List


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        diff = []
        length = len(nums)
        for i in range(length):
            cnt1 = len(set(nums[:i+1]))
            cnt2 = len(set(nums[i+1:]))
            diff.append(cnt2-cnt1)
        return diff

