from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        temp = nums[-k:] + nums[:length-k]
        for i in range(length):
            nums[i] = temp[i]



if __name__ == '__main__':
    nums = [-1,-100,3,99]
    k = 2
    s = Solution()
    s.rotate(nums, k)