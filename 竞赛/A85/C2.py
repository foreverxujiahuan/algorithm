from typing import List
import string

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        lowercase = string.ascii_lowercase
        length = len(s)
        ch2index = {lowercase[i]: i for i in range(len(lowercase))}
        index2ch = {i: lowercase[i] for i in range(len(lowercase))}
        d = {i: 0 for i in range(length)}
        for shift in shifts:
            start, end, direction = shift
            for i in range(start, end+1):
                if direction == 0:
                    d[i] -= 1
                else:
                    d[i] += 1
        ans = ''
        for i, ch in enumerate(s):
            new_index = (ch2index[ch] + d[i]) % 26
            new_ch = index2ch[new_index]
            ans += new_ch
        return ans


if __name__ == '__main__':
    solution = Solution()
    s = "abc"
    shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
    # s = "dztz"
    # shifts = [[0, 0, 0], [1, 1, 1]]
    res = solution.shiftingLetters(s, shifts)
    print(res)