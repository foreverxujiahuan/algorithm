from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = len(arr1)
        for a1 in arr1:
            flag = 0
            for a2 in arr2:
                if abs(a1-a2) <= 2:
                    flag = 1
            ans -= flag
        return ans
