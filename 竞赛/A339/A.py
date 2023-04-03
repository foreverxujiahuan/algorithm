class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans = 0
        for i in range(1, 26):
            tmp = '0' * i + '1' * i
            if tmp in s:
                ans = i * 2
        return ans