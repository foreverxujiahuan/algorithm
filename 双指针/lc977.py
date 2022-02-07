from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        neg = -1
        for i, num in enumerate(nums):
            if num < 0:
                neg = i
            else:
                break
        i = neg
        j = neg + 1
        res = []
        while i >= 0 or j < n:
            if i < 0:
                res.append(nums[j] ** 2)
                j += 1
            elif j == n:
                res.append(nums[i] ** 2)
                i -= 1
            elif abs(nums[i]) < abs(nums[j]):
                res.append(nums[i] ** 2)
                i -= 1
            else:
                res.append(nums[j] ** 2)
                j += 1
        return res

