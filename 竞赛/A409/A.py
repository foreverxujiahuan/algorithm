from typing import List


class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid)


    def adjacentSum(self, value: int) -> int:
        ans = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == value:
                    if i-1 >= 0:
                        ans += self.grid[i-1][j]
                    if i+1 < self.m:
                        ans += self.grid[i+1][j]
                    if j-1 >= 0:
                        ans += self.grid[i][j-1]
                    if j+1 < self.n:
                        ans += self.grid[i][j+1]
        return ans

    def diagonalSum(self, value: int) -> int:
        ans = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == value:
                    if i-1 >= 0 and j-1 >= 0:
                        ans += self.grid[i-1][j-1]
                    if i+1 < self.m and j+1 < self.n:
                        ans += self.grid[i + 1][j+1]
                    if j-1 >= 0 and i+1 < self.m:
                        ans += self.grid[i+1][j - 1]
                    if j + 1 < self.n and i-1 >= 0:
                        ans += self.grid[i-1][j + 1]
        return ans



# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)