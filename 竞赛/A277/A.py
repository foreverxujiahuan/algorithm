from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        max_v = max(nums)
        min_v = min(nums)
        res = 0
        for i in range(len(nums)):
            if min_v < nums[i] < max_v:
                res += 1
        return res

if __name__ == '__main__':
    nums = [-3,3,3,90]
    so = Solution()
    res = so.countElements(nums)
    print(res)