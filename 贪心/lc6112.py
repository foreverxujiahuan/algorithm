from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        ans = 0
        while sum(amount) != 0:
            amount.sort()
            cnt = 0
            if amount[2] > 0:
                amount[2] -= 1
                cnt += 1
            if amount[1] > 0 and cnt < 2:
                amount[1] -= 1
                cnt += 1
            if amount[0] > 0 and cnt < 2:
                amount[0] -= 1
                cnt += 1
            ans += 1
        return ans


if __name__ == '__main__':
    amount = [5,4,4]
    solution = Solution()
    res = solution.fillCups(amount)
    print(res)