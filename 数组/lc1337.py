from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d = dict()
        for i in range(len(mat)):
            d[i] = sum(mat[i])
        temp = sorted(d.items(), key=lambda d:d[1])
        return [t[0] for t in temp[:k]]
