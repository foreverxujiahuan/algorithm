from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        i_one = []
        i_zero = []
        j_one = []
        j_zero = []
        m, n = len(grid), len(grid[0])
        for t in grid:
            one_num = sum(t)
            i_one.append(one_num)
            i_zero.append(n-one_num)
        temp = []

        for j in range(n):
            t = []
            for i in range(m):
                t.append(grid[i][j])
            temp.append(t)

        for t in temp:
            one_num = sum(t)
            j_one.append(one_num)
            j_zero.append(m-one_num)

        diff = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                diff[i][j] = i_one[i] + j_one[j] - i_zero[i] - j_zero[j]
        return diff

if __name__ == '__main__':
    grid = [[0, 1, 1], [1, 0, 1], [0, 0, 1]]
    solution = Solution()
    res = solution.onesMinusZeros(grid)
    print(res)