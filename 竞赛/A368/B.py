from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        length = len(nums)
        pre = nums[:]
        pos = nums[:]
        for i in range(1, length):
            mi = min(pre[i-1], nums[i])
            pre[i] = mi
        for i in range(length-2, -1, -1):
            mi = min(pos[i+1], nums[i])
            pos[i] = mi
        ans = 9999234999
        for i in range(1, length-1):
            if nums[i] > pre[i-1] and nums[i] > pos[i+1]:
                ans = min(ans, nums[i] + pre[i-1] + pos[i+1])
        if ans != 9999234999:
            return ans
        return -1


if __name__ == '__main__':
    solution = Solution()
    nums = [5,4,8,7,10,2]
    res = solution.minimumSum(nums)
    print(res)