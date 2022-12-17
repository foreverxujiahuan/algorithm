from typing import List


class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        s = sum(nums)
        target = goal - s
        ans = abs(target) // abs(limit)
        if abs(target) % abs(limit) != 0:
            ans += 1
        return ans


if __name__ == '__main__':
    nums = [1, -10, 9, 1]
    limit = 100
    goal = 0
    solution = Solution()
    res =solution.minElements(nums, limit, goal)
    print(res)
