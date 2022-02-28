from typing import List


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        length = len(nums1)
        for i in range(length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    if nums1[k] in set(nums2[nums2.index(nums1[j]):]) and nums1[j] in\
                            set(nums2[nums1.index(j): nums1.index(k)]) and nums1[i] in set(nums2[:nums2.index(j)]):
                        res += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    nums1 = [4,0,1,3,2]
    nums2 = [4,1,0,2,3]
    res = solution.goodTriplets(nums1, nums2)
    print(res)