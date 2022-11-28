from typing import List


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        ans = 0
        g = [[] for _ in range(len(roads) + 1)]
        for x, y in roads:
            g[x].append(y)
            g[y].append(x)
        def dfs(x: int, fa: int) -> int:
            size = 1
            for y in g[x]:
                if y != fa:
                    size += dfs(y, x)
            if x:
                nonlocal ans
                ans += (size + seats - 1) // seats
            return size
        dfs(0, -1)
        return ans


if __name__ == '__main__':
    roads = [[0, 1], [0, 2], [0, 3]]
    seats = 5
    solution = Solution()
    res = solution.minimumFuelCost(roads, seats)
    print(res)