from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        nums_set = nums1_set.intersection(nums2_set)
        if nums_set:
            return min(nums_set)
        mi1, mi2 = min(nums1), min(nums2)
        t1 = mi1 + 10 * mi2
        t2 = mi2 + 10 * mi1
        ans = min(t2, t1)
        return ans