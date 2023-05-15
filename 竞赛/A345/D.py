from typing import List
from collections import defaultdict


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        graph2 = defaultdict(set)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            graph2[x].add(y)
            graph2[y].add(x)

        visited = set()

        def dfs(i):
            visited.add(i)
            cur.append(i)
            for j in graph[i]:
                if j not in visited:
                    dfs(j)

        res = []
        for i in range(n):
            if i not in visited:
                cur = []
                dfs(i)
                res.append(cur)
        ans = 0
        for t in res:
            flag = True
            length = len(t)
            for i in range(length):
                for j in range(i+1, length):
                    a, b = t[i], t[j]
                    if not (a in graph2[b] or b in graph2[a]):
                        flag = False
            if flag:
                ans += 1
        return ans


if __name__ == '__main__':
    n = 6
    edges = [[0, 1], [0, 2], [1, 2], [3, 4]]
    # edges = [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]
    solution = Solution()
    res = solution.countCompleteComponents(n, edges)
    print(res)