from typing import List
from collections import defaultdict


class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        row2ones = dict()
        col2ones = defaultdict(int)
        m, n = len(grid), len(grid[0])
        for i, row in enumerate(grid):
            row2ones[i] = row.count(1)
        for j in range(n):
            for i in range(m):
                col2ones[j] += grid[i][j]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += (row2ones[i] - 1) * (col2ones[j] - 1)
        return ans


if __name__ == '__main__':
    solution = Solution()
    grid = [[0,1,0],[0,1,1],[0,1,0]]
    res = solution.numberOfRightTriangles(grid)
    print(res)

