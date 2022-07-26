class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n+1
        while l < r:
            mid = l + r >> 1
            if mid * (mid + 1) <= 2 * n:
                l = mid
            else:
                r = mid - 1
        return l


