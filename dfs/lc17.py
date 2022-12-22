from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = {
            '0': '',
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        ans = []
        cur = ''
        i = 0
        def dfs(i, cur, ans):
            if i == len(digits):
                ans.append(cur)
                return
            for c in d[digits[i]]:
                dfs(i+1, cur+c, ans)
        dfs(i, cur, ans)
        return ans


if __name__ == '__main__':
    digits = "23"
    solution = Solution()
    res = solution.letterCombinations(digits)
    print(res)