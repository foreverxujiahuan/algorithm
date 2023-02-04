from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for query in queries:
            cur = 0
            for point in points:
                x1, y1, r = query
                x2, y2 = point
                if (x1 -x2) ** 2 + (y1 - y2) ** 2 <= r ** 2:
                    cur += 1
            ans.append(cur)
        return ans


if __name__ == '__main__':
    points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    queries = [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]
    solution = Solution()
    res = solution.countPoints(points, queries)
    print(res)
