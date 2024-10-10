from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right_most = nums[0]
        for i in range(len(nums)):
            if i <= right_most:
                right_most = max(right_most, i + nums[i])
        return right_most >= len(nums) - 1


nums = [1,2,3]
ans = Solution().canJump(nums)
print(ans)