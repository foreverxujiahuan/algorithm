from typing import List


class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        ans = 0
        rows = [0] * n
        cols = [0] * n
        for t, i, v in queries:
            if t == 0:
                ans += (v - rows[i]) * n
                rows[i] = v
            else:
                ans += (v - cols[i]) * n
                cols[i] = v
        return ans

if __name__ == '__main__':
    n = 3
    queries = [[0, 0, 1], [1, 2, 2], [0, 2, 3], [1, 0, 4]]
    solution = Solution()
    res = solution.matrixSumQueries(n, queries)
    print(res)