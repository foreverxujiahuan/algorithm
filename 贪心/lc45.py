from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return 0
        step = 0
        index = 0
        while index < length:
            if index + nums[index] >= length - 1:
                step += 1
                break
            start = index + 1
            end = index + nums[index] + 1
            index = self.get_max(nums, start, end)
            step += 1
            if nums[index] == 0:
                break
            if index == length - 1:
                break
            if index + nums[index] >= length:
                step += 1
                break
        return step

    def get_max(self, nums, start, end):
        if start >= len(nums):
            return start - 1
        max_index = start
        max_value = nums[start]
        for i in range(start, min(len(nums), end)):
            if nums[i] + i >= max_value:
                max_index = i
                max_value = nums[i] + i
        return max_index


if __name__ == '__main__':
    s = Solution()
    nums = [10,9,8,7,6,5,4,3,2,1,1,0]
    res = s.jump(nums)
    print(res)
