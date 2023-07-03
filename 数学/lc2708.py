from typing import List


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        pos_nums = [n for n in nums if n > 0]
        zero_nums = [n for n in nums if n == 0]
        neg_nums = [n for n in nums if n < 0]
        if pos_nums:
            pos_ans = pos_nums[0]
            for i in range(1, len(pos_nums)):
                pos_ans = pos_ans * pos_nums[i]
        if neg_nums:
            neg_nums.sort()
            if len(neg_nums) % 2 == 0:
                neg_ans = neg_nums[0]
                for i in range(1, len(neg_nums)):
                    neg_ans = neg_ans * neg_ans[i]
            else:
                neg_ans = neg_nums[0]
                for i in range(1, len(neg_nums)-1):
                    neg_ans = neg_ans * neg_ans[i]
        if pos_nums and neg_nums:
            pass