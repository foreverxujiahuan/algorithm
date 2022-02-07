from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        for i in range(len(spaces)):
            index = spaces[i] + i
            s = s[:index] + ' ' + s[index:]
        return s


s = "spacing"
spaces = [0,1,2,3,4,5,6]
solution  = Solution()
res = solution.addSpaces(s, spaces)
print(res)
