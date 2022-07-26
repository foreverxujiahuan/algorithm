from heapq import heappop, heappush
from typing import List
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        ans = []
        pq = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, m))]
        while pq and len(ans) < k:
            _, i, j = heappop(pq)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans


if __name__ == '__main__':
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    solution = Solution()
    res = solution.kSmallestPairs(nums1, nums2, k)
    print(res)

