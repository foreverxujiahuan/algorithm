class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        t1 = ""
        t2 = ""
        for c in s:
            if c == '#':
                t1 = t1[:-1]
            else:
                t1 += c
        for c in t:
            if c == '#':
                t2 = t2[:-1]
            else:
                t2 += c
        return t1 == t2



if __name__ == '__main__':
    s = "ab#c"
    t = "ad#c"
    solution = Solution()
    res = solution.backspaceCompare(s, t)
    print(res)