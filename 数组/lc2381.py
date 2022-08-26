import string
from itertools import accumulate
from string import ascii_lowercase
from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        lowercase = string.ascii_lowercase
        ch2index = {lowercase[i]: i for i in range(len(lowercase))}
        index2ch = {i: lowercase[i] for i in range(len(lowercase))}
        diff = [0] * (len(s) + 1)
        for shift in shifts:
            start, end, direction = shift
            if direction == 0:
                diff[start] -= 1
                diff[end+1] += 1
            else:
                diff[start] += 1
                diff[end+1] -= 1
        d = list(accumulate(diff))
        ans = ''
        for i, ch in enumerate(s):
            new_index = (ch2index[ch] + d[i]) % 26
            new_ch = index2ch[new_index]
            ans += new_ch
        return ans


if __name__ == '__main__':
    s = "abc"
    shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
    solution = Solution()
    res = solution.shiftingLetters(s, shifts)
    print(res)
