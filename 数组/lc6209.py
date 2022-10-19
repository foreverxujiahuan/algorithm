from typing import List
import math


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        x = int(math.log(n, 2))
        powers = []
        while x >= 0:
            a, b = divmod(n, 2 ** x)
            if a != 0:
                powers.append(2 ** x)
            n = b
            x -= 1
        powers = list(reversed(powers))
        ans = []
        for q in queries:
            t = 1
            for i in range(q[0], q[1] + 1):
                t *= powers[i]
            ans.append(int(t % (1e9 + 7)))
        return ans


if __name__ == '__main__':
    n = 919
    queries = [[0, 6]]
    solution = Solution()
    res = solution.productQueries(n, queries)
    print(res)
