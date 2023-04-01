class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = 0
        while k > 0:
            if numOnes:
                k -= 1
                ans += 1
            elif numZeros:
                k -= 1
            else:
                ans -= 1
                k -= 1
        return ans
