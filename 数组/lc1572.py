from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        if n % 2 == 1:
            mid = n // 2
            ans -= mat[mid][mid]
        for i in range(n):
            ans += mat[i][i]
            ans += mat[i][n-i-1]
        return ans

if __name__ == '__main__':
    solution = Solution()
    mat = [[1,2,3],
            [4,5,6],
            [7,8,9]]
    res = solution.diagonalSum(mat)
    print(res)

