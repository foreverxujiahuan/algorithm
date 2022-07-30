from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        length1 = len(nums1)
        length2 = len(nums2)
        ans = 0
        for i in range(length1):
            l, r = i, length2
            while l < r:
                mid = l + r >> 1
                if nums1[i] <= nums2[mid]:
                    if mid - i > ans:
                        ans = mid - i
                    l = mid + 1
                else:
                    r = mid
        return ans


if __name__ == '__main__':
    nums1 = [30,29,19,5]
    nums2 = [25,25]
    solution = Solution()
    res = solution.maxDistance(nums1, nums2)
    print(res)

