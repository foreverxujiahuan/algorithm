from typing import List


class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        # 初始化邻接矩阵
        INF = float('inf')
        graph = [[INF] * n for _ in range(n)]
        for u, v in edges:
            graph[u][v] = graph[v][u] = 1

        # Floyd算法求解最短路径
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

        # 遍历每个顶点的所有出边，寻找最短环
        res = INF
        for u in range(n):
            for v in range(n):
                if graph[u][v] == 2:
                    for w in range(n):
                        if graph[u][w] == 1 and graph[v][w] == 1:
                            res = min(res, graph[u][v] + graph[u][w] + graph[v][w] - 6)
        return res if res != INF else -1


if __name__ == '__main__':
    n = 7
    edges = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 6], [6, 3]]
    solution = Solution()
    res = solution.findShortestCycle(n, edges)
    print(res)