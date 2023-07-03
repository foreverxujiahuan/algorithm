from typing import List


class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                top_left = []
                bottom_right = []
                cur_x, cur_y = i-1, j-1
                while cur_x >= 0 and cur_y >= 0:
                    top_left.append(grid[cur_x][cur_y])
                    cur_x -= 1
                    cur_y -= 1
                cur_x, cur_y = i + 1, j + 1
                while cur_x < m and cur_y < n:
                    bottom_right.append(grid[cur_x][cur_y])
                    cur_x += 1
                    cur_y += 1
                ans[i][j] = abs(len(set(top_left)) - len(set(bottom_right)))
        return ans

if __name__ == '__main__':
    grid = [[1,2,3],[3,1,5],[3,2,1]]
    solution = Solution()
    res = solution.differenceOfDistinctValues(grid)
    print(res)