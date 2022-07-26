from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        arr = []
        for t in mat:
            arr += t
        m, n = len(mat), len(mat[0])
        if m*n != r*c:
            return mat
        ans = [[0 for _ in range(c)] for _ in range(r)]
        index = 0
        for i in range(r):
            for j in range(c):
                ans[i][j] = arr[index]
                index += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    mat = [[1,2],[3,4]]
    r, c = 2, 2
    res = solution.matrixReshape(mat, r, c)
    print(res)
