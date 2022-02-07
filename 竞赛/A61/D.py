from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums = sorted(nums)
        length = len(nums)
        if length % 2 == 0:
            return self.f1(nums)
        else:
            return self.f2(nums)

    def f1(self, nums):
        length = len(nums)
        mid1 = length // 2
        mid2 = (length // 2) - 1
        count1, count2 = 0, 0
        to_arr1 = [i for i in range(nums[mid1] - mid1, nums[mid1])] + [i for i in range(nums[mid1], nums[mid1] + mid1)]
        to_arr2 = [i for i in range(nums[mid2] - mid2, nums[mid2])] + [i for i in range(nums[mid2], nums[mid2] + mid2)]
        for t in nums:
            if t not in to_arr1:
                count1 += 1
        for t in nums:
            if t not in to_arr2:
                count2 += 1
        return min(count1, count2)

    def f2(self, nums):
        length = len(nums)
        mid = length // 2
        count = 0
        to_arr = [i for i in range(nums[mid] - mid, nums[mid])] + [i for i in range(nums[mid], nums[mid] + mid + 1)]
        for t in nums:
            if t not in to_arr:
                count += 1
        return count


if __name__ == '__main__':
    nums = [8,5,9,9,8,4]
    s = Solution()
    res = s.minOperations(nums)
    print(res)