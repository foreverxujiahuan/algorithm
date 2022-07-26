class Solution:
    def appealSum(self, s: str) -> int:
        ans, sum_g, pos = 0, 0, [-1] * 26
        for i, c in enumerate(s):
            c = ord(c) - ord('a')
            sum_g += i + 1 if pos[c] < 0 else i - pos[c]
            ans += sum_g
            pos[c] = i
        return ans


if __name__ == '__main__':
    solution = Solution()
    s = ""
    res = solution.appealSum(s)
    print(res)