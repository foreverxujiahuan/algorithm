class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1, num2 = self.f(num1), self.f(num2)
        return str(num2 * num1)

    def f(self, s):
        d = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }
        flag = 1
        ans = 0
        for c in reversed(s):
            ans += d[c] * flag
            flag *= 10
        return ans