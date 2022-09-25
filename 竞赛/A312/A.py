from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        temp = [(name, height) for name, height in zip(names, heights)]
        temp.sort(key=lambda d:d[1], reverse=True)
        ans = [t[0] for t in temp]
        return ans




