from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]
        zeros = [(i, j) for i in range(m) for j in range(n) if mat[i][j] == 0]
        seen = set(zeros)
        queue = deque(zeros)
        while queue:
            i, j = queue.popleft()
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    ans[ni][nj] = ans[i][j] + 1
                    queue.append((ni, nj))
                    seen.add((ni, nj))
        return ans


if __name__ == '__main__':
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    solution = Solution()
    res = solution.updateMatrix(mat)
    print(res)
