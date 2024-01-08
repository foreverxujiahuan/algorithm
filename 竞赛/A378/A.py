from typing import List


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        cnt = len([n for n in nums if n % 2 == 0])
        return cnt >= 2
