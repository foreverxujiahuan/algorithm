from typing import List
from collections import defaultdict

from sortedcontainers import SortedList


class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        if not edges:
            return max(vals)
        edge2valid_edges = dict()
        for edge in edges:
            i, j = edge
            if i not in edge2valid_edges.keys():
                edge2valid_edges[i] = []
            if j not in edge2valid_edges.keys():
                edge2valid_edges[j] = []
            edge2valid_edges[i].append(vals[j])
            edge2valid_edges[j].append(vals[i])
        mx = 1e-99
        length = len(vals)
        for edge in range(length):
            arr = sorted(edge2valid_edges.get(edge, []), reverse=True)[:k]
            t1 = vals[edge]
            t2 = sum([v for v in arr if v > 0])
            mx = max(mx, t1 + t2)

        return mx


if __name__ == '__main__':
    vals = [1, 2, 3, 4, 10, -10, -20]
    edges = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [3, 6]]
    k = 2
    # vals = [-14, -12, -24, 20, -4]
    # edges = [[1, 3], [2, 4], [0, 4], [3, 0]]
    # k = 3
    # vals = [1, -8, 0]
    # edges = [[1,0], [2,1]]
    # k = 2
    # vals = [0, -36, 4, 35, 27, -13]
    # edges = [[5, 3], [4, 3], [0, 4], [2, 4], [0, 2]]
    # k = 1
    solution = Solution()
    ans = solution.maxStarSum(vals, edges, k)
    print(ans)