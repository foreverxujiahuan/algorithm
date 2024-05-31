

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        d1, d2 = dict(), dict()
        for i, c in enumerate(s):
            d1[c] = i
        for i, c in enumerate(t):
            d2[c] = i
        ans = 0
        for k, v in d1.items():
            ans += abs(d1[k] - d2[k])
        return ans