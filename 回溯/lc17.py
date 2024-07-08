from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = {"2": "abc",
             "3": "def",
             "4": "ghi",
             "5": "jkl",
             "6": "mno",
             "7": "pqrs",
             "8": "tuv",
             "9": "wxyz"}
        ans = []

        def dfs(cur, i):
            if len(cur) == len(digits):
                ans.append(cur)
                return
            for c in d[digits[i]]:
                dfs(cur + c, i+1)
        dfs("", 0)
        return ans


if __name__ == '__main__':
    solution = Solution()
    digits = "2"
    res = solution.letterCombinations(digits)
    print(res)

