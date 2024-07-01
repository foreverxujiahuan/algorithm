from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        x_point = []
        y_point = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x_point.append(i)
                    y_point.append(j)
        mi_x, mx_x = min(x_point), max(x_point)
        mi_y, mx_y = min(y_point), max(y_point)
        ans = (mx_x - mi_x + 1) * (mx_y - mi_y + 1)
        return ans
