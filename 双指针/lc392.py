class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        i = 0
        j = 0
        while j != len(t):
            if i == len(s):
                break
            if t[j] == s[i]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(s)


if __name__ == '__main__':
    s = "b"
    t = "abc"
    solution = Solution()
    res = solution.isSubsequence(s, t)
    print(res)