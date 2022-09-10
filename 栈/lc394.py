class Solution:
    def decodeString(self, s: str) -> str:
        ans = ''
        t = ''
        n = ''
        flag = 0
        for ch in s:
            if ch == '[':
                flag = 1
            elif ch == ']':
                ans += int(n) * t
                n = ''
                t = ''
                flag = 0
            elif ch in '0123456789':
                n += ch
            else:
                if flag == 0:
                    ans += ch
                else:
                    t += ch
        return ans

if __name__ == '__main__':
    s = "3[a2[c]]"
    solution = Solution()
    res = solution.decodeString(s)
    print(res)