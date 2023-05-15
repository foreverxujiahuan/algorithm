from typing import List


class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        ans = 0
        length = len(nums)
        for i in range(length):
            nums[i] = sorted(nums[i], reverse=True)
        m, n = len(nums), len(nums[0])
        for j in range(n):
            cur = []
            for i in range(m):
                cur.append(nums[i][j])
            ans += max(cur)
        return ans

if __name__ == '__main__':
    nums = [[1]]
    solution = Solution()
    res = solution.matrixSum(nums)
    print(res)