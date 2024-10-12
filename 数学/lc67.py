
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_a = self.f(a)
        sum_b = self.f(b)
        n = sum_a + sum_b
        ans = ""
        while n:
            if n % 2 == 1:
                ans = "1" + ans
            else:
                ans = "0" + ans
            n = n // 2
        if not ans:
            return "0"
        return ans

    def f(self, s: str):
        flag = 1
        ans = 0
        for c in reversed(s):
            if c == '1':
                ans += flag
            flag *= 2
        return ans

a = "1010"
b = "1011"
ans = Solution().addBinary(a,b)
print(ans)