from typing import List


class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            if k % 2 == 0:
                return nums[0]
            else:
                return -1
        if k == 0:
            return nums[0]
        if k == 1:
            if len(nums) == 1:
                return -1
            else:
                return nums[1]
        else:
            if k < len(nums):
                return max(max(nums[:k-1]), nums[k])
            elif k == len(nums):
                return max(nums[:k-1])
            else:
                return max(nums)


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    k = 4
    s = Solution()
    res = s.maximumTop(nums, k)
    print(res)