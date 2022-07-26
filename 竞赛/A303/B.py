from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = []
        n = len(grid)
        for i in range(n):
            t = []
            for j in range(n):
                t.append(grid[j][i])
            cols.append(t)
        ans = 0
        for col in cols:
            for row in grid:
                if col == row:
                    ans += 1
        return ans


if __name__ == '__main__':
    grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    solution = Solution()
    res = solution.equalPairs(grid)
    print(res)