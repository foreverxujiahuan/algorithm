from typing import List
from torch.nn.init import kaiming_normal
from collections import defaultdict
d = defaultdict()

class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        ans = 0
        length = len(energyDrinkA)
        flag = None
        i = 0
        while i < length:
            if not flag:
                if energyDrinkA[i] > energyDrinkB[i]:
                    ans += energyDrinkA[i]
                    flag = 'A'
                elif energyDrinkA[i] < energyDrinkB[i]:
                    ans += energyDrinkB[i]
                    flag = 'B'
                else:
                    if i+2 < length and energyDrinkA[i+1] + energyDrinkA[i+2] >= energyDrinkB[i+1] + energyDrinkB[i+2]:
                        ans += energyDrinkA[i]
                        flag = 'A'
                    else:
                        ans += energyDrinkB[i]
                        flag = 'B'
                i += 1
            elif flag == 'A':
                if i+1 < length and energyDrinkB[i+1] > energyDrinkA[i] + energyDrinkA[i+1]:
                    ans += energyDrinkB[i+1]
                    i += 2
                    flag = 'B'
                else:
                    ans += energyDrinkA[i]
                    i += 1
            elif flag == 'B':
                if i+1 < length and energyDrinkA[i+1] > energyDrinkB[i] + energyDrinkB[i+1]:
                    ans += energyDrinkA[i+1]
                    i += 2
                    flag = 'A'
                else:
                    ans += energyDrinkB[i]
                    i += 1
        return ans


if __name__ == '__main__':
    energyDrinkA = [3,5,6]
    energyDrinkB = [5,3,5]
    solution = Solution()
    res = solution.maxEnergyBoost(energyDrinkA, energyDrinkB)
    print(res)