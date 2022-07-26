from typing import List


class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        counts = []
        for point in points:
            count = 0
            for rectangle in rectangles:
                if point[0] <= rectangle[0] and point[1] <= rectangle[1]:
                    count += 1
            counts.append(count)
        return counts

if __name__ == '__main__':
    pass
