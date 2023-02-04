from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        diff = [nums1[i] - nums2[i] for i in range(len(nums1))]
        if nums1 == nums2:
            return 0
        if k == 0:
            return -1
        cnt_list = [t / k for t in diff]
        for cnt in cnt_list:
            if int(cnt) != cnt:
                return -1
        if sum(cnt_list) != 0:
            return -1
        cnt_list = [int(t) for t in cnt_list]
        return sum([t for t in cnt_list if t > 0])

if __name__ == '__main__':
    # nums1 = [4, 3, 1, 4]
    # nums2 = [1, 3, 7, 1]
    # k = 3
    nums1 = [3, 8, 5, 2]
    nums2 = [2, 4, 1, 6]
    k = 1
    solution = Solution()
    res = solution.minOperations(nums1, nums2, k)
    print(res)
