from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        length = len(arr)
        target = arr[1] - arr[0]
        for i in range(1, length):
            if arr[i] - arr[i-1] != target:
                return False
        return True