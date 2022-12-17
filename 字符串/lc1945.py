from string import ascii_lowercase

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        d = {ascii_lowercase[i]: i+1 for i in range(len(ascii_lowercase))}
        t = ''
        for c in s:
            t += str(d[c])
        t = int(t)
        for _ in range(k):
            t = sum([int(ch) for ch in str(t)])
        return t


