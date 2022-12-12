from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        arr = []
        for a, b in boxTypes:
            t = [b] * a
            arr.extend(t)
        arr.sort(reverse=True)
        return sum(arr[: truckSize])