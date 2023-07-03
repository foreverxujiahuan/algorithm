from typing import List


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        length = len(nums)
        mi = min(nums)
        mx = max(nums)
        mi_index, mx_index = -1, -1
        for i, n in enumerate(nums):
            if n == mi:
                mi_index = i
                break
        for i in range(length-1, -1, -1):
            if nums[i] == mx:
                mx_index = i
                break
        tmp = 0
        if mi_index > mx_index:
            tmp = 1
        ans = mi_index + (length - mx_index - 1) - tmp
        return ans


if __name__ == '__main__':
    solution = Solution()
    nums = [3,2,1]
    res = solution.semiOrderedPermutation(nums)
    print(res)