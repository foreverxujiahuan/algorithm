from collections import Counter


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counter = Counter(moves)
        return counter.get("U") == counter.get("D") and counter.get("L") == counter.get("R")