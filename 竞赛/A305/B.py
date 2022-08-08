from typing import List


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        g = [[] for _ in range(n)]
        for i, j in edges:
            g[i].append(j)
            g[j].append(i)

        ans = 0
        size = 0
        restricted = set(restricted)

        def dfs(x: int) -> None:
            nonlocal size
            nonlocal visited
            visited[x] = True
            size += 1
            for y in g[x]:
                if y not in restricted and not visited[y]:
                    dfs(y)

        visited = [False for _ in range(n)]
        size = 0
        dfs(0)
        ans = max(size, ans)
        return ans


if __name__ == '__main__':
    n = 7
    edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]]
    restricted = [4,2,1]
    solution = Solution()
    res = solution.reachableNodes(n, edges, restricted)
    print(res)