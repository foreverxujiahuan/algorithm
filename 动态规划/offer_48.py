class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = ""
        max_value = 0
        for c in s:
            while c in cur:
                cur = cur[1:]
            cur = cur + c
            if len(cur) > max_value:
                max_value = len(cur)
        return max_value


if __name__ == '__main__':
    s = "pwwkew"
    sol = Solution()
    res = sol.lengthOfLongestSubstring(s)
    print(res)