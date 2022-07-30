import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = math.sqrt(c)
        n = int(n) + 1
        for i in range(n):
            l, r = 0, n
            while l < r:
                mid = l + r >> 1
                t1 = mid ** 2 + i ** 2
                if t1 == c:
                    return True
                elif t1 > c:
                    r = mid
                else:
                    l = mid + 1
        return False


if __name__ == '__main__':
    c = 0
    solution = Solution()
    res = solution.judgeSquareSum(c)
    print(res)

