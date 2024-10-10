from typing import List
from itertools import accumulate
import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        cur = nums[:k]
        heapq.heapify(cur)
        ans.append(heapq.heappop(cur))
        for i in range(k+1, len(nums)):
            heapq.heappush(cur, -nums[i])
            ans.append(-heapq.heappop(cur))
        return ans

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    res = solution.maxSlidingWindow(nums, k)
    print(res)