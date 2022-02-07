from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums = sorted(nums)
        length = len(nums)
        mid = int(length/2)
        if length % 2 == 0:
            return (nums[mid-1] + nums[mid]) / 2
        return nums[mid]


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1]
    nums2 = []
    res = solution.findMedianSortedArrays(nums1, nums2)
    print(res)
