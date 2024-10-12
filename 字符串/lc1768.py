class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        if len(word1) >= len(word2):
            mi = len(word2)
            for c1, c2 in zip(word1, word2):
                ans += c1
                ans += c2
            ans += word1[mi:]
        else:
            mi = len(word1)
            for c1, c2 in zip(word1, word2):
                ans += c1
                ans += c2
            ans += word2[mi:]
        return ans

if __name__ == '__main__':
    solution = Solution()
    word1 = "ab"
    word2 = "pqrs"
    res = solution.mergeAlternately(word1, word2)
    print(res)
