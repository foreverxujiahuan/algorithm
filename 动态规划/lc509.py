class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a


if __name__ == '__main__':
    solution = Solution()
    res = solution.fib(3)
    print(res)