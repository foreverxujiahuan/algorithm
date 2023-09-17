from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        length = len(nums)
        ans = 0
        for i in range(length):
            bin_i = bin(i)[2:]
            cnt = bin_i.count("1")
            if cnt == k:
                ans += nums[i]
        return ans

if __name__ == '__main__':
    solution = Solution()
    nums = [5, 10, 1, 5, 2]
    k = 1
    res = solution.sumIndicesWithKSetBits(nums, k)
    print(res)
