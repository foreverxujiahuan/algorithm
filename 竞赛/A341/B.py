from typing import List


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        ans = min(divisors)
        mx_value = 0
        for d in divisors:
            cur_value = 0
            for n in nums:
                if n % d == 0:
                    cur_value += 1
            if cur_value > mx_value:
                ans = d
                mx_value = cur_value
            if cur_value == mx_value and d < ans:
                ans = d
        return ans