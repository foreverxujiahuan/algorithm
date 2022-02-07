import math

class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        a = 2 ** p - 1
        b = 2 ** p - 2
        c = (2 ** (p-1) - 1)
        return a * pow(b, c, 1000000007) % 1000000007


if __name__ == '__main__':
    s = Solution()
    p = 22
    res = s.minNonZeroProduct(p)
    print(res)
    # print(2**4 - 1)