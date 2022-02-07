class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        l1 = len(s)
        l2 = len(t)
        dp = [[0 for i in range(l1+1)] for j in range(l2+1)]
        for i in range(l1+1):
            dp[0][i] = 1
        for i in range(1, l2+1):
            for j in range(1, l1+1):
                if s[j-1] == t[i-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[l2][l1]


if __name__ == '__main__':
    s = "aabb"
    t = "ab"
    solution = Solution()
    res = solution.numDistinct(s, t)
    print(res)
