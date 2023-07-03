class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        ans = min(x, y) * 4 + (1+z) * 2
        return min(ans, (x+y+z) * 2)


