from typing import List


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        ans, scores = 0, [0] * len(edges)
        for i, to in enumerate(edges):
            scores[to] += i
            if scores[to] > scores[ans] or scores[to] == scores[ans] and to < ans:
                ans = to
        return ans


if __name__ == '__main__':
    edges = [2,0,0,2]
    solution = Solution()
    res = solution.edgeScore(edges)
    print(res)