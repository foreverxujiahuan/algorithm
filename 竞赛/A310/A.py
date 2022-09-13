from collections import Counter
from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_v = 0
        ans = -1
        for k, v in counter.items():
            if k % 2 != 0:
                continue
            if v > max_v:
                ans = k
                max_v = v
            if v == max_v and k < ans:
                ans = k
        return ans

if __name__ == '__main__':
    solution = Solution()