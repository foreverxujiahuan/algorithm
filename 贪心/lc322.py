from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = 0
        a = list()
        coins.sort(reverse=True)
        for coin in coins:
            if amount >= coin:
                n = amount // coin
                ans += n
                amount -= n * coin
        if amount != 0:
            return -1
        return ans


if __name__ == '__main__':
    coins = [186,419,83,408]
    amount = 6249
    solution = Solution()
    res = solution.coinChange(coins, amount)
    print(res)