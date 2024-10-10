

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1, d2 = dict(), dict()
        for ch1, ch2 in zip(s, t):
            if ch1 in d1:
                if d1[ch1] != ch2:
                    return False
            if ch2 in d2:
                if d2[ch2] != ch1:
                    return False
            if ch1 not in d1:
                d1[ch1] = ch2
            if ch2 not in d2:
                d2[ch2] = ch1
        return True


s = "badc"
t = "baba"
ans = Solution().isIsomorphic(s, t)
print(ans)