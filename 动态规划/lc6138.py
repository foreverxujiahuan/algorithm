class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        f = [0] * 26
        for c in s:
            c = ord(c) - ord('a')
            f[c] = 1 + max(f[max(c - k, 0): c + k + 1])
        return max(f)

