from typing import List
from collections import defaultdict


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        grid = defaultdict(set)
        for invocation in invocations:
            x, y = invocation
            grid[x].add(y)

        error_function = set()

        def dfs(x):
            error_function.add(x)
            for p in grid[x]:
                if p not in error_function:
                    dfs(p)

        dfs(k)

        for invocation in invocations:
            x, y = invocation
            if x not in error_function and y in error_function:
                return list(range(n))

        return list(set(range(n)) - error_function)

