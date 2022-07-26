import collections
from typing import List

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        fathers = {i: i for i in range(n)}

        def get_f(t):
            while not t == fathers[t]:
                fathers[t] = fathers[fathers[t]]
                t = fathers[t]
            return t

        for a, b in edges:
            fathers[get_f(a)] = get_f(b)
        ct = collections.Counter()
        for i in range(n):
            ct[get_f(i)] += 1
        to_ret = 0
        for v in ct.values():
            to_ret += v * (n - v)
        return to_ret // 2


if __name__ == '__main__':
    solution = Solution()
    n = 7
    edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
    res = solution.countPairs(n, edges)
    print(res)
