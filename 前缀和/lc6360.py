from collections import defaultdict
from itertools import accumulate
from typing import List


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        num2indexs = defaultdict(list)
        for i, n in enumerate(nums):
            num2indexs[n].append(i)
        ans = [0 for _ in nums]
        for a in num2indexs.values():
            s = list(accumulate(a, initial=0))
            n = len(a)
            for j, target in enumerate(a):
                left = j * target - s[j]
                right = s[n] - s[j] - target * (n - j)
                ans[target] = left + right
        return ans


if __name__ == '__main__':
    nums = [1, 3, 1, 1, 2]
    solution = Solution()
    res = solution.distance(nums)
    print(res)
