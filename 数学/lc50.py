
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 0
        flag = False
        if n < 0:
            flag = True
            n = - n
        ans = 1
        while n != 1:
            if n % 2 != 0:
                ans *= x
            x *= x
            n = n // 2
        ans *= x
        if flag:
            ans = 1 / ans
        return ans

if __name__ == '__main__':
    solution = Solution()
    x = 0.44528
    n = 0
    res = solution.myPow(x, n)
    print(res)
