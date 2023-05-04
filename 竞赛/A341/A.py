from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = [0, 0]
        for i, row, in enumerate(mat):
            if row.count(1) > ans[1]:
                ans = [i, row.count(1)]
        return ans
