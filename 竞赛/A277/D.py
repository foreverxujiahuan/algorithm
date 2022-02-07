from typing import List


class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        res2 = 0
        # 假设0是好人
        good_set1 = set()
        bad_set1 = set()
        good_set1.add(0)
        for i in range(n):
            if statements[0][i] == 1:
                good_set1.add(i)
            elif statements[0][i] == 0:
                bad_set1.add(i)
        for i in range(1, n):
            for j in range(n):
                pass
        # 假设0是坏人
        pass
        good_set2 = set()
        bad_set2 = set()
        return max(len(good_set1), len(good_set2))