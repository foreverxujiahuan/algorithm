from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rows = [set() for _ in range(m)]
        cols = [set() for _ in range(n)]
        n2index = dict()
        for i in range(m):
            for j in range(n):
                n2index[mat[i][j]] = (i, j)
        for i, num in enumerate(arr):
            x, y = n2index[num]
            rows[x].add(y)
            cols[y].add(x)
            if len(rows[x]) == n or len(cols[y]) == m:
                return i
        return 0


if __name__ == '__main__':
    arr = [2,8,7,4,1,3,5,6,9]
    mat = [[3,2,5],[1,4,6],[8,7,9]]
    solution = Solution()
    res = solution.firstCompleteIndex(arr, mat)
    print(res)
