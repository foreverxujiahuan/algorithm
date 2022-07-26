from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            if grid[i][i] == 0:
                return False
            else:
                grid[i][i] = -1
        for i in range(n-1, -1, -1):
            j = n-i-1
            if grid[i][j] == 0:
                return False
            else:
                grid[i][j] = -1
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0 and grid[i][j] != -1:
                    return False
        return True


if __name__ == '__main__':
    grid = []
    solution = Solution()
    res = solution.checkXMatrix(grid)
    print(res)
