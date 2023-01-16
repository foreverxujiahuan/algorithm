from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        arr = [[0 for _ in range(n)] for _ in range(n)]
        for query in queries:
            row1, col1, row2, col2 = query
            for i in range(row1, row2):
                for j in range(col1, col2):
                    arr[i][j] += 1
        return arr
