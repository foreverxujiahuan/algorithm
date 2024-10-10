from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start_nums = []
        nums = set(nums)
        for n in nums:
            if n-1 not in nums:
                start_nums.append(n)
        ans = 0
        for start in start_nums:
            cur_num = start
            cur_length = 1
            while cur_num + 1 in nums:
                cur_num += 1
                cur_length += 1
            ans = max(ans, cur_length)
        return ans
