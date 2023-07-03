from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        length = len(s)
        dictionary = set(dictionary)
        dp = [0 for _ in range(length+1)]
        for i in range(length):
            dp[i+1] = dp[i] + 1
            for j in range(i+1):
                if s[j: i+1] in dictionary:
                    dp[i+1] = min(dp[i+1], dp[j])
        return dp[length]


if __name__ == '__main__':
    s = "leetscode"
    dictionary = ["leet", "code", "leetcode"]
    solution = Solution()
    res = solution.minExtraChar(s, dictionary)
    print(res)