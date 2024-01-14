from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        mx = max(counter.values())
        ans = 0
        for k, v in counter.items():
            if v == mx:
                ans += v
        return ans

if __name__ == '__main__':
    nums = [1,2,2,3,3]
    solution = Solution()
    res = solution.maxFrequencyElements(nums)
    print(res)