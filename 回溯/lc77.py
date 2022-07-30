from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(start):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start, n - (k - len(path)) + 2):
                path.append(i)
                backtracking(i + 1)
                path.pop()

        path = []
        res = []
        backtracking(1)
        return res


