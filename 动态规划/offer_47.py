from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        grid2 = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                grid2[i+1][j+1] = grid[i][j]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = max((dp[i-1][j-1] + grid2[i-1][j] + grid2[i][j]),
                               (dp[i-1][j-1] + grid2[i][j-1] + grid2[i][j]),
                               (dp[i][j-1] + grid2[i][j]),
                               (dp[i-1][j] + grid2[i][j]))
        return dp[m][n]


if __name__ == '__main__':
    s = Solution()
    grid = [[1,2,3],[4,5,6]]
    res = s.maxValue(grid)
    print(res)
