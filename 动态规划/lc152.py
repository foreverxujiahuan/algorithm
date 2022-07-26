from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = [0 for _ in nums]
        dp_max[0] = nums[0]
        dp_min = [0 for _ in nums]
        dp_min[0] = nums[0]
        length = len(nums)
        for i in range(1, length):
            if nums[i] >= 0:
                dp_max[i] = max(nums[i], nums[i] * dp_max[i-1])
                dp_min[i] = min(nums[i], nums[i] * dp_min[i-1])
            else:
                dp_max[i] = max(nums[i], nums[i] * dp_min[i-1])
                dp_min[i] = min(nums[i], nums[i] * dp_max[i-1])
        return max(dp_max)


if __name__ == '__main__':
    nums = [2, 3, -2, 4]
    solution = Solution()
    res = solution.maxProduct(nums)
    print(res)