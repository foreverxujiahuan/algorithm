from typing import List


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = []
        nums_set = set(nums)
        single_set = set()
        nums.sort()
        for i in range(1, length-1):
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                single_set.add(nums[i])
        if nums.count(nums[0]) == 1:
            single_set.add(nums[0])
        if nums.count(nums[length-1]) == 1:
            single_set.add(nums[length-1])
        for n in nums:
            if n+1 not in nums_set and n-1 not in nums_set and n in single_set:
                res.append(n)
        return res

if __name__ == '__main__':
    nums = [10,6,5,8]
    solution = Solution()
    res = solution.findLonely(nums)
    print(res)
