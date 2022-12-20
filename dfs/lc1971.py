from typing import List

# 图模版题

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = [[] for _ in range(n)]
        for i, j in edges:
            g[i].append(j)
            g[j].append(i)

        valid = set()
        visited = [False for _ in range(n)]

        def dfs(x):
            nonlocal valid
            if visited[x]:
                return
            visited[x] = True
            valid.update(set(g[x]))
            for y in g[x]:
                dfs(y)
        dfs(source)
        return destination in valid or source == destination


if __name__ == '__main__':
    n = 10
    edges = [[4, 3], [1, 4], [4, 8], [1, 7], [6, 4], [4, 2], [7, 4], [4, 0], [0, 9], [5, 4]]
    source = 5
    destination = 9
    solution = Solution()
    res = solution.validPath(n, edges, source, destination)
    print(res)
