from typing import List


class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        transactions.sort(key=lambda d: d[1] - d[0])
        ans = 0
        for transaction in transactions:
            cost, cashback = transaction
            if cost - cashback > ans:
                ans += cost - cashback
            else:
                ans += cost
                break
        return ans


if __name__ == '__main__':
    transactions = [[2, 1], [5, 0], [4, 2]]
    solution = Solution()
    res = solution.minimumMoney(transactions)
    print(res)