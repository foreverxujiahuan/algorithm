from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans, prod, i = 0, 1, 0
        for j, num in enumerate(nums):
            prod *= num
            while i <= j and prod >= k:
                prod //= nums[i]
                i += 1
            ans += j - i + 1
        return ans

if __name__ == '__main__':
    nums = [10,5,2,6]
    k = 100
    solution = Solution()
    res = solution.numSubarrayProductLessThanK(nums, k)
    print(res)