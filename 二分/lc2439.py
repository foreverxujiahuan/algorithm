from bisect import bisect_left
from typing import List


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def check(k):
            have = 0
            for n in nums:
                if n <= k:
                    have += k -n
                else:
                    if have < n - k:
                        return False
                    else:
                        have -= (n - k)
            return True
        l, r = 0, max(nums)
        while l < r:
            mid = (l + r) >> 1
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return r




if __name__ == '__main__':
    nums = [3, 7, 1, 6]
    solution = Solution()
    res = solution.minimizeArrayValue(nums)
    print(res)