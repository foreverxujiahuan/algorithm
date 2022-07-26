from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for i, j in edges:
            g[i].append(j)
            g[j].append(i)

        visited = [False for _ in range(n)]
        tot = 0
        ans = 0
        size = 0

        def dfs(x: int) -> None:
            nonlocal size
            visited[x] = True
            size += 1
            for y in g[x]:
                if not visited[y]:
                    dfs(y)

        for i in range(n):
            if not visited[i]:
                size = 0
                dfs(i)
                ans += size * tot
                tot += size
        return ans


if __name__ == '__main__':
    n = 7
    edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
    solution = Solution()
    res = solution.countPairs(n, edges)
    print(res)

