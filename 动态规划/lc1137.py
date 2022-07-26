class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        for i in range(3, n + 1):
            t = dp[i - 3] + dp[i - 1] + dp[i - 2]
            dp.append(t)
        return dp[n]


if __name__ == '__main__':
    solution = Solution()
    n = 4
    res = solution.tribonacci(n)
    print(res)