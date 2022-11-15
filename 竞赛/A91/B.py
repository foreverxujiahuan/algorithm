class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        def dfs(cur, add):
            nonlocal ans
            if sum(cur) >= high:
                return
            cur.append(add)
            if low <= sum(cur) <= high:
                ans += 1
            for add in [zero, one]:
                dfs(cur, add)

        ans = 0
        dfs([], zero)
        dfs([], one)
        ans = ans % (1e9 + 7)
        ans = int(ans)
        return ans


if __name__ == '__main__':
    low = 3
    high = 3
    zero = 1
    one = 2
    solution = Solution()
    res = solution.countGoodStrings(low, high, zero, one)
    print(res)

