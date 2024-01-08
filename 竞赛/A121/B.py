from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = nums[0]
        for i in range(1, len(nums)):
            s = s ^ nums[i]
        d = s ^ k
        ans = bin(d).count('1')
        return ans


if __name__ == '__main__':
    solution = Solution()
    nums = [2,0,2,0]
    k = 0
    res = solution.minOperations(nums, k)
    print(res)