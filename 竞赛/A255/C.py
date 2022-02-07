import math
from typing import List


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        n = len(mat)
        f = {0}
        for i in range(n):
            g = set()
            for j in mat[i]:
                for x in f:
                    g.add(x+j)
            f = g
        ans = float('inf')
        for t in f:
            ans = min(ans, abs(t-target))
        return ans

    def test(self, mat: List[List[int]], target: int):
        m, n = len(mat), len(mat[0])
        # 什么都不选时和为 0
        f = {0}
        for i in range(m):
            g = set()
            for x in mat[i]:
                for j in f:
                    g.add(j + x)
            f = g

        ans = float("inf")
        for x in f:
            ans = min(ans, abs(x - target))
        return ans

if __name__ == '__main__':
    mat = [[1,2,9,8,7]]
    target = 6
    s = Solution()
    res = s.minimizeTheDifference(mat, target)
    print(res)