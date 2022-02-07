from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        length = len(nums)
        ans = float('inf')
        for i in range(length - k + 1):
            if nums[i+k-1] - nums[i] < ans:
                ans = nums[i+k-1] - nums[i]
        return ans


if __name__ == '__main__':
    nums = [90]
    k = 1
    s = Solution()
    res = s.minimumDifference(nums, k)
    print(res)
