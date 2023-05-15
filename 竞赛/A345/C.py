from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        mx = 0
        m, n = len(grid), len(grid[0])
        def dfs(x, y, grid):
            nonlocal visited
            visited[x][y] = True
            nonlocal cur
            cur = max(cur, y)
            for cur_x, cur_y in [(x-1, y+1), (x, y+1), (x+1, y+1)]:
                if 0 <= cur_x < m and 0 <= cur_y < n and visited[cur_x][cur_y] is False and grid[x][y] < grid[cur_x][cur_y]:
                    dfs(cur_x, cur_y, grid)
        for i in range(m):
            visited = [[False for _ in range(n)] for _ in range(m)]
            cur = 0
            dfs(i, 0, grid)
            mx = max(mx, cur)
        return mx


if __name__ == '__main__':
    grid = [[3,2,4],[2,1,9],[1,1,7]]
    solution = Solution()
    res = solution.maxMoves(grid)
    print(res)
