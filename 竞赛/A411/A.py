class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans = 0
        length = len(s)
        for i in range(length):
            for j in range(i+1, length+1):
                sub = s[i:j]
                if sub.count("0") <= k or sub.count("1") <= k:
                    ans += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    s = "11111"
    k = 1
    res = solution.countKConstraintSubstrings(s, k)
    print(res)