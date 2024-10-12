from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        xi_set, yi_set = {xi for xi, yi in coordinates}, {yi for xi, yi in coordinates}
        if len(xi_set) == 1 or len(yi_set) == 1:
            return True
        point1, point2 = coordinates[0], coordinates[1]
        x1, y1 = point1
        x2, y2 = point2
        if x2 - x1 != 0:
            k = (y2-y1) / (x2 - x1)
        else:
            k = 0
        b = y1 - x1 * k
        for point in coordinates:
            xi, yi = point
            if yi != k * xi + b:
                return False
        return True


if __name__ == '__main__':
    ans = Solution().checkStraightLine([[0,0],[0,1],[0,-1]])
    print(ans)