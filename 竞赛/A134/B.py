from collections import Counter
from typing import List


class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        counter = Counter(enemyEnergies)
        mi = min(counter.keys())
        power = currentEnergy
        if power < mi:
            return 0
        for k, v in counter.items():
            if k == mi:
                power += k * (v-1)
            else:
                power += k * v
        ans = power // mi
        return ans

if __name__ == '__main__':
    solution = Solution()
    enemyEnergies = [1,2, 3]
    currentEnergy = 0
    res = solution.maximumPoints(enemyEnergies, currentEnergy)
    print(res)