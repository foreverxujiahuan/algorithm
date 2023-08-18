class Solution:
    def finalString(self, s: str) -> str:
        ans = ""
        for c in s:
            if c == 'i':
                ans = reversed(ans)
            else:
                ans += c
        return ans