from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res = []
        for n in nums:
            if n < pivot:
                res.append(n)
        for n in nums:
            if n == pivot:
                res.append(n)
        for n in nums:
            if n > pivot:
                res.append(n)
        return res


if __name__ == '__main__':
    nums = [-3,4,3,2]
    pivot = 2
    solution = Solution()
    res = solution.pivotArray(nums, pivot)
    print(res)