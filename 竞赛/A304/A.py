from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        while sum(nums) != 0:
            cnt += 1
            t = min([k for k in nums if k != 0])
            for i in range(n):
                nums[i] = max(0, nums[i] - t)
        return cnt


if __name__ == '__main__':
    nums = [0]
    solution = Solution()
    res = solution.minimumOperations(nums)
    print(res)