from typing import List
import copy


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        # 移动两步
        m, n = len(grid), len(grid[0])
        row2maxvalue = [[0 for _ in range(n)] for _ in range(m)]
        col2maxvalue = [[0 for _ in range(n)] for _ in range(m)]
        row2minvalue = copy.deepcopy(grid)
        col2minvalue = copy.deepcopy(grid)

        for i in range(m):
            for j in range(n-2, -1, -1):
                row2maxvalue[i][j] = max(row2maxvalue[i][j+1], grid[i][j+1])
                row2minvalue[i][j] = min(row2minvalue[i][j-1], grid[i][j-1])
        for i in range(n):
            for j in range(m-2, -1, -1):
                col2maxvalue[j][i] = max(col2maxvalue[j+1][i], grid[j+1][i])
                col2minvalue[i][j] = min(col2minvalue[j-1][i], grid[j-1][i])
        candidate = []
        for i in range(m):
            for j in range(n):
                t1 = row2maxvalue[i][j] - col2minvalue[i][j]
                t2 = col2maxvalue[i][j] - row2minvalue[i][j]
                candidate.append(max(t1, t2))

        # 移动一步,横着
        for i in range(m):
            for j in range(n-1):
                candidate.append(row2maxvalue[i][j] - grid[i][j])
        # 移动一步，竖着
        for j in range(n):
            for i in range(m-1):
                candidate.append(col2maxvalue[i][j] - grid[i][j])
        return max(candidate)


if __name__ == '__main__':
    solution = Solution()
    grid =  [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]
    res = solution.maxScore(grid)
    print(res)




