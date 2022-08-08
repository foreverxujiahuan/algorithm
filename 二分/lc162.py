from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        nums.insert(0, -9999999999999999999999)
        nums.append(-9999999999999999999999)
        while l < r:
            mid = l + r >> 1
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid-1
            elif nums[mid-1] < nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return len(nums) - 3


if __name__ == '__main__':
    nums = [1, 2]
    solution = Solution()
    res = solution.findPeakElement(nums)
    print(res)