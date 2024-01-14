from bisect import bisect_left, bisect_right


class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if x <= y:
            return y - x
        ans = x - y  # 总操作次数不会超过 x-y
        visited = set()
        q = [x]

        def add(v):
            if v not in visited:
                q.append(v)
                visited.add(v)

        step = 0
        while True:
            tmp = q
            q = []
            for v in tmp:
                if v == y:
                    return min(ans, step)
                if v % 5 == 0:
                    add(v // 5)
                if v % 11 == 0:
                    add(v // 11)
                add(v+1)
                add(v-1)
            step += 1


if __name__ == '__main__':
    solution = Solution()
    res = solution.minimumOperationsToMakeEqual(18, 1)
    print(res)