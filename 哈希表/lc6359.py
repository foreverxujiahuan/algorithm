from collections import Counter
from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        counter = Counter(nums)
        keys = list(sorted(counter.keys()))
        ans = 0
        for key in keys:
            if counter[key] >= 2 and p > 0:
                counter[key] -= 2
                p -= 1
        if p == 0:
            return ans
        cur = [k for k in counter.keys() if counter[k] != 0]
        cur.sort()
        i = 0
        while p:
            ans += abs(cur[i] - cur[i+1])
            p -= 1
            i += 2
        return ans


if __name__ == '__main__':
    nums = [8,9,1,5,4,3,6,4,3,7]
    p = 4
    solution = Solution()
    res = solution.minimizeMax(nums, p)
    print(res)