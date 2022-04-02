from typing import List


class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        res = 0
        dig_set = set()
        for d in dig:
            dig_set.add((d[0], d[1]))
        for artifact in artifacts:
            points = set()
            for i in range(artifact[0], artifact[2]+1):
                for j in range(artifact[1], artifact[3]+1):
                    points.add((i, j))
            if points.issubset(dig_set):
                res += 1
        return res


if __name__ == '__main__':
    n = 5
    artifacts = [[3, 1, 4, 1], [1, 1, 2, 2], [1, 0, 2, 0], [4, 3, 4, 4], [0, 3, 1, 4], [2, 3, 3, 4]]
    dig = [[0, 0], [2, 1], [2, 0], [2, 3], [4, 3], [2, 4], [4, 1], [0, 2], [4, 0], [3, 1], [1, 2], [1, 3], [3, 2]]
    s = Solution()
    res = s.digArtifacts(n, artifacts, dig)
    print(res)