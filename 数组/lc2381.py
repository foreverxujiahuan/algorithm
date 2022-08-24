from itertools import accumulate
from string import ascii_lowercase
from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        c2i = {c: i for i, c in enumerate(ascii_lowercase)}
        diff = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            diff[start] += direction * 2 - 1
            diff[end + 1] -= direction * 2 - 1
        return ''.join(ascii_lowercase[(c2i[c] + shift) % 26] for c, shift in zip(s, accumulate(diff)))


if __name__ == '__main__':
    s = "abc"
    shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
    solution = Solution()
    res = solution.shiftingLetters(s, shifts)
    print(res)
