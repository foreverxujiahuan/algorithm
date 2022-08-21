from collections import Counter
from typing import List
import string
import numpy as np

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        d = [0] * (n + 1)
        for start, end, direction in shifts:
            if direction == 1:
                d[start] += 1
                d[end + 1] -= 1
            else:
                d[start] -= 1
                d[end + 1] += 1
        for i in range(1, n + 1):
            d[i] += d[i - 1]

        lowercase = string.ascii_lowercase
        ch2index = {lowercase[i]: i for i in range(len(lowercase))}
        index2ch = {i: lowercase[i] for i in range(len(lowercase))}
        ans = ''
        for i, ch in enumerate(s):
            new_index = (ch2index[ch] + d[i]) % 26
            new_ch = index2ch[new_index]
            ans += new_ch
        return ans


if __name__ == '__main__':
    solution = Solution()
    # s = "abc"
    # shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
    s = "dztz"
    shifts = [[0, 0, 0], [1, 1, 1]]
    res = solution.shiftingLetters(s, shifts)
    print(res)