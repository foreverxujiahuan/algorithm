from collections import Counter
from typing import List
import heapq


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        ans = 0
        while k > 0:
            cur = heapq.heappop(nums)
            ans += -cur
            heapq.heappush(nums, self.f(cur))
            k -= 1
        return ans

    def f(self, n):
        n = -n
        if n % 3 == 0:
            ans = n // 3
        else:
            ans = (n // 3) + 1
        return - ans

if __name__ == '__main__':
    nums = [10,10,10,10,10]
    k = 5
    solution = Solution()
    res = solution.maxKelements(nums, k)
    print(res)
