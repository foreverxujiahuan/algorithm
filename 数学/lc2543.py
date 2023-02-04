from math import gcd


class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        g = gcd(targetX, targetY)
        while g > 1:
            g = g / 2
        return g == 1


if __name__ == '__main__':
    x, y = 4, 7
    ans = Solution().isReachable(targetX=x, targetY=y)
    print(ans)