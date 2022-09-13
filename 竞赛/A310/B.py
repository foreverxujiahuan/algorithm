class Solution:
    def partitionString(self, s: str) -> int:
        ans = 0
        cur = ''
        i, j = 0, 0
        length = len(s)
        while i < length and j < length:
            if s[j] in cur:
                i = j
                ans += 1
                cur = ''
            else:
                cur += s[j]
                j += 1
        if cur:
            ans += 1
        return ans

if __name__ == '__main__':
    s = "abacaba"
    solution = Solution()
    res = solution.partitionString(s)
    print(res)