from typing import List
from itertools import accumulate


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        length = len(energy)

        candidate = []
        for j in range(k):
            temp = []
            for i in range(length-1-j, -1, -k):
                temp.append(energy[i])
            pre_sum = list(accumulate(temp))
            candidate.append(max(pre_sum))
        return max(candidate)


if __name__ == '__main__':
    solution = Solution()
    energy = [5,-10,4,3,5,-9,9,-7]
    k = 2
    res = solution.maximumEnergy(energy, k)
    print(res)