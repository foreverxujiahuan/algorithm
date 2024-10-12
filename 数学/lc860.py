from typing import List
from collections import defaultdict


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = defaultdict(int)
        for b in bills:
            if b == 5:
                d[5] += 1
            if b == 10:
                if d[5] > 0:
                    d[10] += 1
                    d[5] -= 1
                else:
                    return False
            if b == 20:
                if d[10] > 0 and d[5] > 0:
                    d[10] -= 1
                    d[5] -= 1
                elif d[5] >= 3:
                    d[5] -= 3
                else:
                    return False
        return True

if __name__ == '__main__':
    solution = Solution()
    bills = [5,5,10,10,20]
    res = solution.lemonadeChange(bills)
    print(res)