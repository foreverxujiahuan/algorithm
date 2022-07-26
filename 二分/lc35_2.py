from typing import List
import bisect


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        ans = len(nums)
        while l <= r:
            mid = l + r >> 1
            if target <= nums[mid]:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans


if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 7
    solution = Solution()
    res = solution.searchInsert(nums, target)
    print(res)
