import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        visited = [0] * numCourses
        valid = True

        for info in prerequisites:
            edges[info[1]].append(info[0])

        def dfs(u: int):
            nonlocal valid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    valid = False
                    return
            visited[u] = 2

        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)

        return valid


if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    solution = Solution()
    ans = solution.canFinish(numCourses, prerequisites)
    print(ans)
