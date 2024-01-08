from bisect import bisect_left, bisect_right


class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if x <= y:
            return y - x
        ans = x - y  # 总操作次数不会超过 x-y
        vis = [False] * (x + ans + 1)  # +1 操作至多执行 x-y 次
        q = []
        step = 0

        def add(v: int) -> None:
            if v < y:
                nonlocal ans
                ans = min(ans, step + 1 + y - v)  # 只能执行 +1 操作
            elif not vis[v]:
                vis[v] = True
                q.append(v)

        add(x)
        while True:
            tmp = q
            q = []
            for v in tmp:
                if v == y:
                    return min(ans, step)
                if v % 11 == 0:
                    add(v // 11)
                if v % 5 == 0:
                    add(v // 5)
                add(v - 1)
                add(v + 1)
            step += 1


if __name__ == '__main__':
    solution = Solution()
    res = solution.minimumOperationsToMakeEqual(18, 1)
    print(res)