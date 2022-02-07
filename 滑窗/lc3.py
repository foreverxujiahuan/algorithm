class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        cur_s = ''
        for i in range(len(s)):
            while s[i] in cur_s:
                cur_s = cur_s[1:]
            cur_s = cur_s + s[i]
            if len(cur_s) > max_len:
                max_len = len(cur_s)
        return max_len

s = ""
solution = Solution()
res = solution.lengthOfLongestSubstring(s)
print(res)
