class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        res = 0
        length = len(s)
        for i in range(length):
            for j in range(i+1, length):
                t = int(s[i:j], 2)
                if t <= k and len(s[i:j]) > res:
                    res = len(s[i:j])
        return res


if __name__ == '__main__':
    s = "00101001"
    k = 1
    solution = Solution()
    res = solution.longestSubsequence(s, k)
    print(res)