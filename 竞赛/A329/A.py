class Solution:
    def alternateDigitSum(self, n: int) -> int:
        flag = 1
        ans = 0
        for c in str(n):
            ans += flag * int(c)
            flag = flag * -1
        return ans
