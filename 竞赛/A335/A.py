class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cur = 1
        flag = -1
        while time:
            if cur == n or cur == 1:
                flag = flag * -1
            cur += flag
            time -= 1
        return cur


if __name__ == '__main__':
    n = 4
    time = 7
    solution = Solution()
    res = solution.passThePillow(n, time)
    print(res)