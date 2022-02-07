from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = [False for _ in range(length+1)]
        true_flags = [0]
        for i in range(length+1):
            for true_flag in true_flags:
                if s[true_flag: i] in wordDict:
                    if i not in true_flags:
                        true_flags.append(i)
                    dp[i] = True
        return dp[length]


if __name__ == '__main__':
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    print(len(s))
    wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    solution = Solution()
    res = solution.wordBreak(s, wordDict)
    print(res)
