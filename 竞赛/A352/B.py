from typing import List


class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        primes = set(self.f(n))
        ans = []
        for i in range(n//2 + 1):
            if i in primes and n-i in primes:
                ans.append([i, n-i])
        return ans

    def f(self, n):
        primes = [True] * (n+1)
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p*2, n+1, p):
                    primes[i] = False
            p += 1
        primes = [e for e in range(2, n) if primes[e]]
        return primes

if __name__ == '__main__':
    solution = Solution()
    n = 12
    res = solution.findPrimePairs(n)
    print(res)