class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        cnt = s.count(c)
        ans = sum(range(0, cnt+1))
        return ans