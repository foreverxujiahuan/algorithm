from typing import List

from sortedcontainers import SortedList


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        length = len(nums)
        l = 0
        ans = 0
        tmp = -1
        while l != length - 1:
            cur = SortedList()
            cur.add(nums[l])
            r = l + 1
            while r < length:
                cur.add(nums[r])
                if cur[-1] - cur[0] > 2 or r == length - 1:
                    n = r - l
                    ans += (n * n + n) / 2
                    tmp += 1
                    l += 1
                    break
                r += 1
        return int(ans - tmp)


if __name__ == '__main__':
    solution = Solution()
    nums = [5,4,2,4]
    res = solution.continuousSubarrays(nums)
    print(res)

