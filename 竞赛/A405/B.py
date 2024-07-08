from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        def dfs(cur):
            if len(cur) == n:
                ans.append(cur)
                return
            dfs(cur + '1')
            if not cur or cur[-1] == '1':
                dfs(cur + '0')
        ans = []
        dfs('')
        return ans

if __name__ == '__main__':
    solution = Solution()
    n = 3
    res = solution.validStrings(n)
    print(res)