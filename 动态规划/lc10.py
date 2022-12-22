class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        l1, l2 = len(s), len(p)
        dp = [[False for _ in range(l1+1)] for _ in range(l2+1)]
        for i in range(l1+1):
            dp[0][i] = True
        for i in range(l2+1):
            dp[i][0] = True
        for i in range(l1):
            for j in range(l2):
                if s[j] != '*':
                    if s[i] == s[j] or s[j] == '.':
                        dp[i][j] = dp[i-1][j-1]
                    elif s[i] != s[j]:
                        dp[i][j] = False
                else:
                    if s[i] == p[j-1]:
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-2]
        return dp[-1][-1]


if __name__ == '__main__':
    s = "aa"
    p = "a*"
    solution = Solution()
    res = solution.isMatch(s, p)
    print(res)
