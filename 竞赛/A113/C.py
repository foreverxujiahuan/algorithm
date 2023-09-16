import sys
from typing import List


class Solution:
    def mergeSort(self, coordinates, tmp, l, r, k):
        if l >= r:
            return 0

        mid = (l + r) // 2
        inv_count = self.mergeSort(coordinates, tmp, l, mid, k) + self.mergeSort(coordinates, tmp, mid + 1, r, k)
        i, j, pos = l, mid + 1, l
        while i <= mid and j <= r:
            if not self.f(coordinates[i][0], coordinates[j][0], coordinates[i][1], coordinates[j][1]) == k:
                tmp[pos] = coordinates[i]
                i += 1
                inv_count += (j - (mid + 1))
            else:
                tmp[pos] = coordinates[j]
                j += 1
            pos += 1
        for k in range(i, mid + 1):
            tmp[pos] = coordinates[k]
            inv_count += (j - (mid + 1))
            pos += 1
        for k in range(j, r + 1):
            tmp[pos] = coordinates[k]
            pos += 1
        coordinates[l:r + 1] = tmp[l:r + 1]
        return inv_count

    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        n = len(coordinates)
        tmp = [(0, 0)] * n
        return self.mergeSort(coordinates, tmp, 0, n - 1, k)

    def f(self, x1, x2, y1, y2):
        return (x1 ^ x2) + (y1 ^ y2)

if __name__ == '__main__':
    solution = Solution()
    coordinates = [[27,94],[61,68],[47,0],[100,4],[127,89],[61,103],[26,4],[51,54],[91,26],[98,23],[80,74],[19,93]]
    k = 95
    res = solution.countPairs(coordinates, k)
    print(res)