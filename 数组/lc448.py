from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        cur_nums = set(nums)
        n = len(nums)
        ans = []
        for i in range(1, n+1):
            if i not in cur_nums:
                ans.append(i)
        return ans
