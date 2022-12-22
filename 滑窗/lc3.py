class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx = 0
        cur = ''
        for c in s:
            while c in cur:
                cur = cur[1:]
            cur += c
            mx = max(mx, len(cur))
        return mx


s = "bbbbb"
solution = Solution()
res = solution.lengthOfLongestSubstring(s)
print(res)

