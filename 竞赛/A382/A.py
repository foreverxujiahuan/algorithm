
class Solution:
    def countKeyChanges(self, s: str) -> int:
        ans = 0
        s = s.lower()
        length = len(s)
        for i in range(1, length):
            if s[i] != s[i-1]:
                ans += 1
        return ans
