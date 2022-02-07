import math


class Solution:
    def countPrimes(self, n: int) -> int:
        res = 0
        is_prime = [1 for _ in range(n)]
        for i in range(1, n):
            if is_prime[i]:
                if self.flag(i):
                    res += 1
                    j = 2
                    while j*i < n:
                        is_prime[j*i] = 0
                        j += 1
        return res

    def flag(self, n):
        if n == 1:
            return False
        for i in range(2, int(math.log(n))):
            if n % i == 0:
                return False
        return True


if __name__ == '__main__':
    n = 10
    solution = Solution()
    res = solution.countPrimes(n)
    print(res)
