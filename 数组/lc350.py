from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        for t in nums1_set:
            if t in nums2_set:
                ans += [t] * min(nums1.count(t), nums2.count(t))
        return ans

if __name__ == '__main__':
    pass