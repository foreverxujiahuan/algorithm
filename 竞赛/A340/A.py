from typing import List
import math


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        length = len(nums)
        ans = 0
        for i in range(length):
            for j in range(length):
                if i == j or j == length - i - 1:
                    if self.is_prime(nums[i][j]):
                        ans = max(ans, nums[i][j])
        return ans

    def is_prime(self, n):
        if n > 1:
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for x in range(3, int(math.sqrt(n) + 1), 2):
                if n % x == 0:
                    return False
            return True
        return False