from collections import Counter
from typing import List


class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        counter = Counter()
        for i in range(1, n):
            counter[i] = n-i
        d = abs(x - y)
        keys = counter.keys()
        for k in keys:
            if k > d:
                if (k + d - 1) in counter:
                    counter[k + d - 1] -= 1
                if (k - d + 1) in counter:
                    counter[k - d + 1] += 1
        result = []
        for i in range(n):
            result.append(counter[i + 1] * 2)
        return result

if __name__ == '__main__':
    solution = Solution()
    n = 5
    x = 2
    y = 4
    res = solution.countOfPairs(n, x, y)
    print(res)



