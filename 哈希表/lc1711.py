from collections import Counter
from typing import List


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        counter = Counter(deliciousness)
        ans = 0
        mod = 10 ** 9 + 7
        for k, v in counter.items():
            for i in range(22):
                target = 2 ** i - k
                if target == k:
                    ans += (v - 1) * counter.get(target, 0)
                    ans = ans % mod
                else:
                    ans += v * counter.get(target, 0)
                    ans = ans % mod
        ans = int(ans)
        return ans // 2

if __name__ == '__main__':
    deliciousness = [32] * 100000
    solution = Solution()
    res = solution.countPairs(deliciousness)
    print(res)