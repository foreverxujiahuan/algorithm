from typing import List


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        nodes = set(range(0, n))
        ans = []
        for query in queries:
            s, e = query
            remove_node = set(range(s+1, e))
            nodes -= remove_node
            ans.append(len(nodes)-1)
        return ans


if __name__ == '__main__':
    n = 5
    queries = [[1,3], [2,4]]
    solution = Solution()
    res = solution.shortestDistanceAfterQueries(n, queries)
    print(res)