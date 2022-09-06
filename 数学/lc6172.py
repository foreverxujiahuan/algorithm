class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(n-1):
            s = bin(n, i)
            