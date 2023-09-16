class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        abs_x, abs_y = abs(sx - fx), abs(sy - fy)
        mx_t = abs_x + abs_y
        mi_t = max(abs_x, abs_y)
        if mx_t == mi_t == 0 and t == 1:
            return False
        if mi_t <= t <= mx_t:
            return True
        if t >= mx_t:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    sx = 1
    sy = 2
    fx = 1
    fy = 2
    t = 1
    res = solution.isReachableAtTime(sx,sy,fx,fy, t)
    print(res)