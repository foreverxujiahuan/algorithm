from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        cur = 0
        ans = 0
        banned = set(banned)
        for i in range(1, n+1):
            if i not in banned and cur + i <= maxSum:
                cur = cur + i
                ans += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    banned = [11]
    n = 7
    maxSum = 50
    res = solution.maxCount(banned, n, maxSum)
    print(res)
