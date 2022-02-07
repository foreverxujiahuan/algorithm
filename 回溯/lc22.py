from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(n, 0, 0, res, "")
        return res

    def dfs(self, n, left, right, res, cur):
        if right == n:
            res.append(cur)
            return
        if left < n:
            self.dfs(n, left+1, right, res, cur + '(')
        if left > right:
            self.dfs(n, left, right+1, res, cur+')')


if __name__ == '__main__':
    solution = Solution()
    res = solution.generateParenthesis(3)
    print(res)