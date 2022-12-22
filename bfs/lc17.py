from collections import deque
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
        q = ['']
        for digit in digits:
            cur_q = []
            for c in d[digit]:
                for t in q:
                    cur_q.append(t + c)
            q = cur_q
        return q


if __name__ == '__main__':
    digits = ""
    solution = Solution()
    res = solution.letterCombinations(digits)
    print(res)