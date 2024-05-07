from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        f = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            mi = 999999
            mx = int(sqrt(i))
            for j in range(1, mx + 1):
                mi = min(mi, f[i-j*j])
            f[i] = mi + 1
        return f[n]


if __name__ == '__main__':
    solution = Solution()
    res = solution.numSquares(11)
    print(res)
