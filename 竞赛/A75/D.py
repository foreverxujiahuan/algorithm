class Solution:
    def sumScores(self, s: str) -> int:
        res = 0
        si = ""
        for i in range(len(s)):
            si = s[-(i + 1)] + si
            if si[0] != s[0]:
                continue
            res += self.f(s, si)
        return res

    def f(self, s, si):
        left = 0
        right = len(si)
        ans = 0
        while left <= right:
            mid = ((right - left) // 2) + left
            if si[:mid] == s[:mid]:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans

if __name__ == '__main__':
    s = "babab"
    so = Solution()
    res = so.sumScores(s)
    print(res)