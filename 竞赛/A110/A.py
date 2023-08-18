
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        ans = 100
        a = purchaseAmount // 10
        b = purchaseAmount % 10
        if b > 0:
            a += 1
        return ans - a * 10