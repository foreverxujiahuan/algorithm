from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums = list(set(nums))
        nums_subset = self.subsets(nums)
        ans = 0
        for nums in nums_subset:
            if not nums:
                continue
            diff = set()
            length = len(nums)
            for i in range(length):
                for j in range(i+1, length):
                    diff.add(nums[i] - nums[j])
                    diff.add(nums[j] - nums[i])
            if k not in diff:
                ans += 1
        return ans


    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(depth, start, valuelist):
            res.append(valuelist)
            if depth == len(nums): return
            for i in range(start, len(nums)):
                dfs(depth + 1, i + 1, valuelist + [nums[i]])

        nums.sort()
        res = []
        dfs(0, 0, [])
        return res

if __name__ == '__main__':
    solution = Solution()
    nums = [1]
    k = 1
    res = solution.beautifulSubsets(nums, k)
    print(res)