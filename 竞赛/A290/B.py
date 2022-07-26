from typing import List
import math


class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        res = 0
        max_x = max(c[0] + c[2] for c in circles)
        max_y = max(c[1] + c[2] for c in circles)
        for i in range(max_x + 1):
            for j in range(max_y + 1):
                for circle in circles:
                    if math.sqrt((i - circle[0]) ** 2 + (j - circle[1]) ** 2) <= circle[2]:
                        res += 1
                        break
        return res


if __name__ == '__main__':
    circles = [[6,2,2],[6,8,5],[7,7,7],[1,5,1],[7,1,1],[1,7,1],[7,9,2],[4,2,2],[9,10,6],[9,4,2],[7,5,5],[2,1,1],[3,7,3],[6,3,3],[5,10,4],[3,10,2],[9,5,4],[3,1,1]]
    solution = Solution()
    res = solution.countLatticePoints(circles)
    print(res)