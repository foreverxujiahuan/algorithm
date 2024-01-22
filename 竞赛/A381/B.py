from typing import List
from collections import Counter


class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        counter = Counter()
        mx = max([x, y])
        mi = min([x, y])
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                if i == j:
                    continue
                d1 = abs(j - i)
                d2 = abs(mi - i) + 1 + abs(mx - j)
                d = min([d1, d2])
                counter[d] += 2
        result = []
        for i in range(n):
            result.append(counter[i+1])
        return result


if __name__ == '__main__':
    soltuion = Solution()
    n = 3
    x = 1
    y = 3
    res = soltuion.countOfPairs(n,x,y)
    print(res)