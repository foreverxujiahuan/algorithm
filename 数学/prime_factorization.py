from typing import List


"""
Write a function that takes as input a *positive integer* and outputs its prime factorization. 

Examples: 
# [2,3,5]
6 -> [2, 3]
7 -> [7] notice 1 does not count as a prime number
# [2,3,5,7]
# [2,3,5]
5 [5]
8 -> [2,2,2]
# [2,3,5,...]
120 -> [2,2,2,3,5]
1 -> [] again, 1 does not count as a prime number
0 -> throws exception 
-1 -> throws exception 


Try to be as space and memory efficient as possible! 

"""


class Solution:

    def prime_factorization_force(self, n: int) -> List[int]:
        if n <= 0:
            raise ValueError("Input must be a positive integer.")
        # O(n^2)
        prime_nums = [i for i in range(2, n+1) if self.is_prime(i)]
        ans = []
        for prime_num in prime_nums:
            while n % prime_num == 0 and n > 1:
                ans.append(prime_num)
                n = n // prime_num
        return ans

    def prime_factorization_sieve(self, n: int) -> List[int]:
        if n <= 0:
            raise ValueError("Input must be a positive integer.")
        prime_nums = self.eratosthenes_sieve(n)
        ans = []
        for prime_num in prime_nums:
            while n % prime_num == 0 and n > 1:
                ans.append(prime_num)
                n = n // prime_num
        return ans

    def is_prime(self, x):
        for i in range(2, x-1):
            if x % i == 0:
                return False
        return True

    def eratosthenes_sieve(self, n):
        prime = [True] * (n + 1)
        prime[0] = prime[1] = False  # 0 和 1 不是质数

        p = 2
        while p * p <= n:
            if prime[p]:
                # 将 p 的所有倍数标记为 False
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1

        # 返回所有质数
        return [p for p in range(n + 1) if prime[p]]

    def prime_factorization(self, n: int) -> List[int]:
        if n <= 0:
            raise ValueError("Input must be a positive integer.")

        factors = []
        # Start with the smallest prime factor
        factor = 2
        # O(logn)
        # O(1)
        while n > 1:
            while n % factor == 0:
                factors.append(factor)
                n = n // factor
            factor += 1

        return factors


if __name__ == '__main__':
    candidates = [6,7,8,120,200]
    solution = Solution()
    for n in candidates:
        ans1 = solution.prime_factorization_force(n)  # 暴力
        ans2 = solution.prime_factorization(n)  # 数学
        ans3 = solution.prime_factorization_sieve(n)  # 质数筛
        print(f"n={n};ans1={ans1};ans2={ans2};ans3={ans3}")
