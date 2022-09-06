from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def find(x):  # 并查集
            if x not in cache:
                cache[x] = x
            if cache[x] != x:
                cache[x] = find(cache[x])
            return cache[x]

        def merge(x, y):  # 合并
            cache[find(x)] = cache[find(y)]

        cache = {}
        for x, y in edges:
            merge(x, y)

        d = {}
        for i in range(n):  # 遍历每个节点
            x = find(i)  # 所属环
            d[x] = d.get(x, 0) + 1
        res = 0

        for k, v in d.items():  # 遍历每个环
            res += v * (n - v)
        return res // 2


if __name__ == '__main__':
    solution = Solution()
    n = 7
    edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
    res = solution.countPairs(n, edges)
    print(res)
