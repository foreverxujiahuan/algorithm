import sys
from collections import Counter
from typing import List


class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        d = Counter()
        ans = 0
        for x, y in coordinates:
            for i in range(k+1):
                tx = x ^ i
                ty = y ^ (k-i)
                ans += d[(tx, ty)]
            d[(x, y)] += 1
        return ans

if __name__ == '__main__':
    solution = Solution()
    coordinates = [[27,94],[61,68],[47,0],[100,4],[127,89],[61,103],[26,4],[51,54],[91,26],[98,23],[80,74],[19,93]]
    k = 95
    res = solution.countPairs(coordinates, k)
    print(res)