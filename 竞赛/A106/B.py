class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        ans = 0
        length = len(s)
        for i in range(length):
            for j in range(i, length+1):
                if self.f(s[i: j]):
                    ans = max(j - i, ans)
        return ans

    def f(self, candidate):
        cnt = 0
        length = len(candidate)
        for i in range(length-1):
            if candidate[i] == candidate[i+1]:
                cnt += 1
        return cnt <= 1


if __name__ == '__main__':
    s = "1111111"
    solution = Solution()
    res = solution.longestSemiRepetitiveSubstring(s)
    print(res)
