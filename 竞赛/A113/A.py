from typing import List


class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        mi = min(nums)
        index = nums.index(mi)
        length = len(nums)
        sorted_nums = sorted(nums)
        if nums == sorted_nums:
            return 0
        if nums[index:] + nums[: index] == sorted_nums:
            return length - index
        return -1

if __name__ == '__main__':
    solution = Solution()
    nums = [1,5,4]
    res = solution.minimumRightShifts(nums)
    print(res)