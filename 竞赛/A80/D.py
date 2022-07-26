from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = s = left = 0
        for right, num in enumerate(nums):
            s += num
            while s * (right - left + 1) >= k:
                s -= nums[left]
                left += 1
            ans += right - left + 1
        return ans


if __name__ == '__main__':
    nums = [1,1,1]
    k = 5
    solution = Solution()
    res = solution.countSubarrays(nums, k)
    print(res)