from collections import Counter
from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = [0 for _ in A]
        length = len(A)
        for i in range(length):
            counter1 = Counter(A[:i+1])
            counter2 = Counter(B[:i+1])
            cur = 0
            for k, v in counter1.items():
                if k in counter2.keys():
                    cur += min(counter1[k], counter2[k])
            ans[i] = cur
        return ans

