from typing import List


class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        cur = []
        m, n = len(grid), len(grid[0])
        def dfs(x, y, grid, path, cur):
            path.append((x, y))
            if x == m-1 and y == n-1:
                cur.append(path)
            for cur_x, cur_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= cur_x < m and 0 <= cur_y < n and grid[cur_x][cur_y] == 1:
                    dfs(cur_x, cur_y, grid, path, cur)
        dfs(0, 0, grid, [], cur)
        if not cur or len(cur) == 1:
            return True
        tmp = {(x, y) for x in range(m) for y in range(n)}
        for c in cur:
            tmp = tmp.intersection(c)
        if tmp:
            return True
        return False

if __name__ == '__main__':
    grid = [[1, 1, 1], [1, 0, 0], [1, 1, 1]]
    solution = Solution()
    res = solution.isPossibleToCutPath(grid)
    print(res)