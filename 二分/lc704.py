from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = ((right - left) // 2) + left
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 2
    solution = Solution()
    res = solution.search(nums, target)
    print(res)
