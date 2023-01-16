from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        ans = 0
        mx = nums[0]
        lm = mx
        for i in range(1, len(nums)):
            if lm > nums[i]:
                ans = i
                lm = mx
            else:
                mx = max(mx, nums[i])
        return ans + 1


if __name__ == '__main__':
    nums = [90,47,69,10,43,92,31,73,61,97]
    solution = Solution()
    res = solution.partitionDisjoint(nums)
    print(res)
