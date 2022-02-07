from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1
        ans = n
        while left <= right:
            mid = ((right - left) // 2) + left
            if target <= nums[mid]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 3, 5, 6]
    target = 0
    res = solution.searchInsert(nums, target)
    print(res)
