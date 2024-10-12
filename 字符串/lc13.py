class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1,
             "V": 5,
             "X": 10,
             "L": 50,
             "C": 100,
             "D": 500,
             "M": 1000}
        ans = 0
        length = len(s)
        for i in range(length):
            ans += d[s[i]]
            if i != 0:
                if s[i] in "VX" and s[i-1] == 'I':
                    ans -= 2
                if s[i] in "LC" and s[i-1] == 'X':
                    ans -= 20
                if s[i] in "DM" and s[i-1] == "C":
                    ans -= 200
        return ans

if __name__ == '__main__':
    s = "MCMXCIV"
    solution = Solution()
    res = solution.romanToInt(s)
    print(res)
