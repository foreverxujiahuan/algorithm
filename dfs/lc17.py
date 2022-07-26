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
        res = []
        cur = ''
        length = len(digits)
        def dfs(num, cur, res):
            if num == length:
                res.append(cur)
                return
            for letter in d[digits[num]]:
                dfs(num + 1, cur + letter, res)
        dfs(0, cur, res)
        return res


if __name__ == '__main__':
    digits = "23"
    solution = Solution()
    res = solution.letterCombinations(digits)
    print(res)