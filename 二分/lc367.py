class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num + 1
        while l < r:
            mid = l+r >> 1
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                r = mid
            else:
                l = mid + 1
        return False
