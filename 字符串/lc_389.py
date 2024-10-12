from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter1 = Counter(s)
        counter2 = Counter(t)
        for k, v in counter2.items():
            if k not in counter1 or counter1[k] < v:
                return k