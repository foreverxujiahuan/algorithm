from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        def dfs(x, y, grid):
            grid[x][y] = '0'
            for cur_x, cur_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= cur_x < m and 0 <= cur_y < n and grid[cur_x][cur_y] == '1':
                    dfs(cur_x, cur_y, grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j, grid)
        return ans

if __name__ == '__main__':
    solution = Solution()
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    res = solution.numIslands(grid=grid)
    print(res)




