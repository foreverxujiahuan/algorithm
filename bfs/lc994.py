from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rotting = {(i, j) for i in range(m) for j in range(n) if grid[i][j] == 2}
        fresh = {(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1}
        ans = 0
        while fresh:
            if not rotting:
                return -1
            rotting = {(i+di, j + dj) for i, j in rotting for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]
                       if (i+di, j + dj) in fresh}
            fresh -= rotting
            ans += 1
        return ans


if __name__ == '__main__':
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    solution = Solution()
    res = solution.orangesRotting(grid)
    print(res)


