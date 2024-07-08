from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        l = 0
        for r in range(n):
            cur = nums[r]

            while l <= r and cur > k:
                l += 1
                cur &= nums[l:r + 1]

            if cur == k:
                ans += r - l + 1

        return ans


if __name__ == '__main__':
    solution = Solution()
    nums = [1,1,2]
    k = 1
    res = solution.countSubarrays(nums, k)
    print(res)