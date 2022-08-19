from typing import List


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        d = dict()
        for i, edge in enumerate(edges):
            if edge in d.keys():
                if i in d.keys():
                    d[edge] = d[edge] | d[i]
                    d[edge].add(i)
                else:
                    d[edge].add(i)
            else:
                d[edge] = {i}

        def dfs(x: int):
            nonlocal size
            nonlocal visited
            visited[x] = True
            size += x
            for y in d.get(x, []):
                if not visited[y]:
                    dfs(y)

        ans, max_value = 0, 0
        for i in range(n):
            visited = [False for _ in range(n)]
            size = 0
            dfs(i)
            if max_value < size:
                max_value = size
                ans = i

        return ans


if __name__ == '__main__':
    solution = Solution()
    # edges = [1,6,9,7,2,4,4,8,9,0] # 4
    edges = [1, 0, 0, 0, 0, 7, 7, 5]
    # edges = [2,0,0,2]
    res = solution.edgeScore(edges)
    print(res)