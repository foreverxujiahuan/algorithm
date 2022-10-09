from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        points = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    points.append([i, j])
        for point in points:
            row, col = point
            for i in range(n):
                matrix[row][i] = 0
            for i in range(m):
                matrix[i][col] = 0
