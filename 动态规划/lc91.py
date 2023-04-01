class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1 for _ in s]
        for i, c in enumerate(s):
            if (i == 0 and c == '0') or (c == '0' and i > 0 and s[i-1] not in '12'):
                return 0
            elif i > 0 and '10' <= s[i-1: i+1] <= '26' and not (i == len(s)-1 and c == '0'):
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = dp[i-1]
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    s = "2101"
    res = solution.numDecodings(s)
    print(res)
