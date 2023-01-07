from itertools import permutations
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        q = [""]
        for _ in range(n * 2):
            cur_q = []
            for c in q:
                cur_q.append(c + "(")
            for c in q:
                cur_q.append(c + ")")
            q = cur_q
        ans = [s for s in q if self.valid(s)]
        return ans

    def valid(self, s):
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if stack:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


if __name__ == '__main__':
    solution = Solution()
    res = solution.generateParenthesis(5)
    print(res)
    # n = 3
    # candidates = permutations("()" * n)
    # print(len(list(candidates)))
    # candidates = set(["".join(t) for t in candidates])
    # print(len(candidates))
    # print(list(candidates))