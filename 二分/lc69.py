class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x+1
        ans = 0
        while l<r:
            mid = l + r >> 1
            if mid * mid == x:
                ans = mid
                r = mid
            elif mid * mid > x:
                ans = mid - 1
                r = mid
            else:
                l = mid + 1
        return ans


if __name__ == '__main__':
    x = 8
    solution = Solution()
    res = solution.mySqrt(x)
    print(res)