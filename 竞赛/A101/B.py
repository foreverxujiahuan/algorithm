from typing import List
from string import ascii_lowercase


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        ch2value = dict()
        for i, c in enumerate(ascii_lowercase):
            if c in chars:
                i = chars.index(c)
                ch2value[c] = vals[i]
            else:
                ch2value[c] = i + 1
        dp = [0]
        for i, c in enumerate(s):
            mx = max(dp[i] + ch2value[c], 0)
            dp.append(mx)
        return max(dp)

if __name__ == '__main__':
    s = "abc"
    chars = "abc"
    vals = [-1, -1, -1]
    solution = Solution()
    res = solution.maximumCostSubstring(s, chars, vals)
    print(res)