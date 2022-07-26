from typing import List
import bisect


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        l = len(potions)
        for spell in spells:
            t = success / spell
            n = bisect.bisect_left(potions, t)
            n = l - n
            res.append(n)
        return res


if __name__ == '__main__':
    spells = [3,1,2]
    potions = [8,5,8]
    success = 16
    solution = Solution()
    res = solution.successfulPairs(spells, potions, success)
    print(res)