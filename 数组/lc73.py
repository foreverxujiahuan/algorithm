from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        flag = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    flag[i][j] = True
        for i in range(m):
            for j in range(n):
                if flag[i][j]:
                    for ii in range(m):
                        matrix[ii][j] = 0
                    for jj in range(n):
                        matrix[i][jj] = 0

Solution().setZeroes(matrix=[[1,1,1],[1,0,1],[1,1,1]])