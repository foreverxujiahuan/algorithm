class Solution:
    def distMoney(self, money: int, children: int) -> int:
        cur = [0 for _ in range(children)]
        for i in range(children):
            if money:
                cur[i] += 1
                money -= 1
        for i in range(children):
            if money >= 7:
                cur[i] += 7
                money -= 7
        if cur.count(0) != 0:
            return -1
        ans = cur.count(8)
        if money == 3 and ans == children - 1:
            return ans - 1
        if money > 0 and ans == children:
            return ans - 1
        return ans


if __name__ == '__main__':
    money = 100
    children = 12
    solution = Solution()
    res = solution.distMoney(money, children)
    print(res)