from collections import Counter
from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n, cnt = len(nums), Counter()
        ans = n * (n - 1) // 2
        for i, num in enumerate(nums):
            cnt[num - i] += 1
        for k, v in cnt.items():
            ans -= sum(range(v))
        return ans


if __name__ == '__main__':
    nums = [4, 1, 3, 3]
    solution = Solution()
    res = solution.countBadPairs(nums)
    print(res)