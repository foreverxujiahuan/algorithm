from typing import List


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        n = len(s)
        for i in range(n):
            for j in range(i+1):
                if s[: i+1].count(s[j]) == 2:
                    return s[j]


if __name__ == '__main__':
    solution = Solution()
    s = "abcdd"
    res = solution.repeatedCharacter(s)
    print(res)