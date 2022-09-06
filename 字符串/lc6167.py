from typing import List
from string import ascii_lowercase


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        for k, index in enumerate(distance):
            target = ascii_lowercase[k]
            index1, index2 = 0, 0
            for i, ch in enumerate(s):
                if ch == target:
                    index1 = i
                    break
            for j, ch in enumerate(s):
                if ch == target and j != index1:
                    index2 = j
                    break
            if index1 == index2 == 0:
                continue
            if index2 - index1 - 1 != index:
                return False
        return True

if __name__ == '__main__':
    s = "abaccb"
    distance = [1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    solution = Solution()
    res = solution.checkDistances(s, distance)
    print(res)