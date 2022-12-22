class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        length = len(s)
        for i, ch in enumerate(s):
            j = 0
            while i-j >= 0 and i+j < length and s[i+j] == s[i-j]:
                if 1 + j * 2 > len(ans):
                    ans = s[i-j: i+j+1]
                j += 1
            j = 0
            while i-1-j >= 0 and i + j < length and s[i] == s[i-1] and s[i+j] == s[i-1-j]:
                if 2 + j * 2 > len(ans):
                    ans = s[i-1-j: i+j+1]
                j += 1
            j = 0
            while i-j >= 0 and i+j+1 < length and s[i] == s[i+1] and s[i+j+1] == s[i-j]:
                if 2 + j * 2 > len(ans):
                    ans = s[i-j: i+j+2]
                j += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    s = "ccc"
    res = solution.longestPalindrome(s)
    print(res)
