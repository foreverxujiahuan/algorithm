class Solution:
    def smallestValue(self, n: int) -> int:

        while n > self.f(n):
            n = self.f(n)
        return n

    def f(self, n):
        for i in range(2, n):
            if n % i == 0:
                return i + int(n // i)
        return n


if __name__ == '__main__':
    n = 12
    solution = Solution()
    res = solution.smallestValue(n)
    print(res)