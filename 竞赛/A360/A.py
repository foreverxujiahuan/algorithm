
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l = moves.count("L")
        r = moves.count("R")
        m = moves.count("_")
        ans = abs(l-r) + m
        return ans