from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = []
        for i in range(1, m-1):
            t = []
            for j in range(1, n-1):
                temp = [grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1],
                        grid[i][j-1], grid[i][j], grid[i][j+1],
                        grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1]]
                t.append(max(temp))
            ans.append(t)
        return ans

if __name__ == '__main__':
    grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    solution = Solution()
    res = solution.largestLocal(grid)
    print(res)