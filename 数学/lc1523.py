
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 1:
            ans = 1 + (high - low) // 2
        else:
            ans = (high - low) // 2
        if high % 2 == 1:
            ans += 1
        return ans
