from collections import defaultdict
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        num2sum = defaultdict(int)
        num2values = defaultdict(list)
        for i in range(len(nums2)):
            num2sum[nums2[i]] += nums1[i]
            num2values[nums2[i]].append(nums1[i])
        mx = -1
        sorted_key = list(sorted(set(nums2)))
        lose = 0
        length = len(nums1)
        for i in range(len(sorted_key) - 1):
            key = sorted_key[i]
            lose += len(num2values[key])
            if length - lose > k:
                continue
            else:
                t1 = sorted_key[i+1]
                t2 = sum([sum(num2values[num]) for num in sorted_key[i+1:]])
                mx = max(t1 * t2, mx)
        return mx


if __name__ == '__main__':
    nums1 = [1,3,3,2]
    nums2 = [2,1,3,4]
    k = 3
    solution = Solution()
    res = solution.maxScore(nums1, nums2, k)
    print(res)

