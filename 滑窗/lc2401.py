from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l, r, n = 0, 1, len(nums)
        ans = 1
        while r < n:
            if nums[l] & nums[r] == 0:
                r += 1
            else:
                l += 1
                r += 1
            ans = max(ans, r - l)
        return ans


if __name__ == '__main__':
    solution = Solution()
    nums = [744437702,379056602,145555074,392756761,560864007,934981918,113312475,1090,16384,33,217313281,117883195,978927664]
    res = solution.longestNiceSubarray(nums)
    print(res)