class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        cur = ""
        for i in range(length):
            cur += s[i]
            if cur * (length // len(cur)) == s and i != length - 1:
                return True
        return False