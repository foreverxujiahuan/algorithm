from math import factorial
from collections import Counter


class Solution:
    def countAnagrams(self, s: str) -> int:
        ans = 1
        p = 10 ** 9 + 7
        for word in s.split():
            val = factorial(len(word))
            arr = Counter(word).values()
            for x in arr:
                val = val * pow(factorial(x), p-2, p)
            ans = (ans * val) % p
        return ans % p

    def f(self, n):
        ans = 1
        for i in range(1, n+1):
            ans = ans * i
        return ans

if __name__ == '__main__':
    s = "smuiquglfwdepzuyqtgujaisius ithsczpelfqp rjm"
    # s = ""
    solution = Solution()
    res = solution.countAnagrams(s)
    print(res)
