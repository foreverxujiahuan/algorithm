class Solution:
    def numWays(self, n: int) -> int:
        a = 0
        b = 1
        for i in range(n):
            a = a % (1000000007)
            b = b % (1000000007)
            a, b = b%(1000000007), a+b%(1000000007)
        return b


if __name__ == '__main__':
    s = Solution()
    res = s.numWays(7)
    print(res)