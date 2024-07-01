from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        flag = False

        for n in nums:
            if (n == 0 and not flag) or (n == 1 and flag):
                ans += 1
                flag = not flag

        return ans


if __name__ == '__main__':
    solution = Solution()
    nums = [0,1,1,0,1]
    res = solution.minOperations(nums)
    print(res)