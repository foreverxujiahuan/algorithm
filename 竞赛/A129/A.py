from typing import List


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        t1 = [grid[0][0], grid[0][1], grid[1][0], grid[1][1]]
        t2 = [grid[1][0], grid[1][1], grid[2][0], grid[2][1]]
        t3 = [grid[0][1], grid[0][2], grid[1][1], grid[1][2]]
        t4 = [grid[1][1], grid[1][2], grid[2][1], grid[2][2]]
        v1 = max(t1.count("B"), t1.count("W"))
        v2 = max(t2.count("B"), t1.count("W"))
        v3 = max(t3.count("B"), t1.count("W"))
        v4 = max(t4.count("B"), t1.count("W"))
        if max([v1, v2, v3, v4]) == 2:
            return False
        return True