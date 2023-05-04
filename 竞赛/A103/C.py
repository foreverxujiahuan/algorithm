from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        def dfs(x, y, grid):
            visited[x][y] = True
            nonlocal cur
            cur += grid[x][y]
            for cur_x, cur_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= cur_x < m and 0 <= cur_y < n and visited[cur_x][cur_y] == False and grid[x][y] != 0:
                    dfs(cur_x, cur_y, grid)

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and not visited[i][j]:
                    cur = 0
                    dfs(i, j, grid)
                    ans = max(ans, cur)

        return ans


if __name__ == '__main__':
    grid = [[10]]
    solution = Solution()
    res = solution.findMaxFish(grid)
    print(res)