from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        i = 0

        while i <= n - 3:
            if nums[i] == 0:
                for j in range(3):
                    nums[i + j] ^= 1
                ans += 1
            i += 1

        for j in range(n - 2, n):
            if nums[j] == 0:
                return -1

        return ans

if __name__ == '__main__':
    soltuion = Solution()
    nums = [0, 1, 1, 1, 0, 0]
    res = soltuion.minOperations(nums)
    print(res)
