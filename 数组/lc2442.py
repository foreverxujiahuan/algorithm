from typing import List


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        valid_set = set()
        for n in nums:
            valid_set.add(n)
            valid_set.add(int(str(n)[::-1]))
        return len(valid_set)