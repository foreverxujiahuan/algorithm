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
        q = []
        for c in digits:
            if not q:
                for t in d.get(c, ""):
                    q.append(t)
            else:
                cur_q = []
                for s1 in q:
                    for s2 in d.get(c, ""):
                        cur_q.append(s1 + s2)
                q = cur_q
        return q


if __name__ == '__main__':
    digits = "29"
    solution = Solution()
    res = solution.letterCombinations(digits)
    print(res)