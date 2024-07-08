from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(cur, l, r):
            if len(cur) == 2 * n:
                ans.append("".join(cur))
                return
            if l < n:
                cur.append("(")
                backtrack(cur, l+1, r)
                cur.pop()
            if r < l:
                cur.append(")")
                backtrack(cur, l, r+1)
                cur.pop()

        ans = []
        backtrack([], 0, 0)
        return ans

if __name__ == '__main__':
    solution = Solution()
    n = 3
    res = solution.generateParenthesis(n)
    print(res)