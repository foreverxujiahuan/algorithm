from collections import defaultdict, Counter
from itertools import accumulate
from typing import List
from math import ceil


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        flag = []
        for n in nums:
            if n % modulo == k:
                flag.append(1)
            else:
                flag.append(0)
        per_sum = list(accumulate(flag))
        per_sum = [0] + per_sum
        length = len(per_sum)
        d = defaultdict(int)
        d[0] = 1
        ans = 0
        for i in range(1, length):
            t = [d[key] for key, v in d.items() if (per_sum[i] - key) % modulo == k]
            s = sum(t)
            ans += s
            d[per_sum[i]] += 1
        return ans


if __name__ == '__main__':
    nums = [3,1,9,6]
    modulo= 3
    k = 0
    solution = Solution()
    res = solution.countInterestingSubarrays(nums, modulo, k)
    print(res)