from typing import List


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = [0 for _ in range(n)]
        for i in range(n):
            cur = 0
            for j in range(m):
                cur = max(cur, len(str(grid[n][m])))
            ans[i] = cur
        return ans
