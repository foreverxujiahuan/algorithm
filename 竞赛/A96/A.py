from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums_set1 = set(nums1)
        nums_set2 = set(nums2)
        tmp = nums_set1.intersection(nums_set2)
        if tmp:
            return min(tmp)
        return -1