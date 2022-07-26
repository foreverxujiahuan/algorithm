from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        flags = [[1 for _ in range(n)] for _ in range(m)]
        wall_set = {(i, j) for i, j in walls}
        guard_set = {(i, j) for i, j in guards}
        for guard in guards:
            flags[guard[0]][guard[1]] = 0
        for wall in walls:
            flags[wall[0]][wall[1]] = 0
        for guard in guards:
            x, y = guard
            for i in range(x+1, m):
                if (i, y) in wall_set or (i, y) in guard_set:
                    break
                flags[i][y] = 0
            for i in range(x-1, -1, -1):
                if (i, y) in wall_set or (i, y) in guard_set:
                    break
                flags[i][y] = 0
            for i in range(y+1, n):
                if (x, i) in wall_set or (x, i) in guard_set:
                    break
                flags[x][i] = 0
            for i in range(y-1, -1, -1):
                if (x, i) in wall_set or (x, i) in guard_set:
                    break
                flags[x][i] = 0
        res = sum([sum(t) for t in flags])
        return res

if __name__ == '__main__':
    solution = Solution()
    m = 4
    n = 6
    guards = [[0,0],[1,1],[2,3]]
    walls = [[0,1],[2,2],[1,4]]
    res = solution.countUnguarded(m, n, guards, walls)
    print(res)
