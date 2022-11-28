class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l1 = len(s)
        l2 = len(t)
        i, j = 0, 0
        while i < l1 and j < l2:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        return l2 - j


if __name__ == '__main__':
    s = "z"
    t = "abcde"
    solution = Solution()
    res = solution.appendCharacters(s, t)
    print(res)

