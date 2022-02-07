from typing import List


class DetectSquares:

    def __init__(self):
        self.points = []


    def add(self, point: List[int]) -> None:
        self.points.append(point)


    def count(self, point: List[int]) -> int:
        points_count = dict()
        for p in self.points:
            if str(p) not in points_count.keys():
                points_count[str(p)] = 1
            else:
                points_count[str(p)] += 1
        x = point[0]
        y = point[1]
        x_points = [point for point in self.points if point[0] == x]
        x_points = sorted(x_points, key=lambda x: x[1])
        for p in x_points:
            points_count[str(p)] -= 1
        res = 0
        for point in x_points:
            dis = abs(point[1] - y)
            if dis == 0:
                continue
            p1 = [x-dis, y]
            p2 = [x-dis, y-dis]
            if points_count.get(str(p1), 0) > 0 and points_count.get(str(p2), 0) > 0:
                res += points_count[str(p1)] * points_count[str(p2)]
            p3 = [x+dis, y]
            p4 = [x+dis, y-dis]
            if points_count.get(str(p3), 0) > 0 and points_count.get(str(p4), 0) > 0:
                res += points_count[str(p3)] * points_count[str(p4)]
            p5 = [x - dis, y + dis]
            p6 = [x - dis, y]
            if points_count.get(str(p5), 0) > 0 and points_count.get(str(p6), 0) > 0:
                res += points_count[str(p5)] * points_count[str(p6)]
            p7 = [x + dis, y + dis]
            p8 = [x + dis, y]
            if points_count.get(str(p7), 0) > 0 and points_count.get(str(p8), 0) > 0:
                res += points_count[str(p7)] * points_count[str(p8)]
        return res


if __name__ == '__main__':
    detectSquares = DetectSquares()
    detectSquares.add([3, 10])
    detectSquares.add([11, 2])
    detectSquares.add([3, 2])
    res = detectSquares.count([11, 10])
    res2 = detectSquares.count([14, 8])
    detectSquares.add([11, 2])
    detectSquares.add([11, 2])
    res3 = detectSquares.count([11, 10])
    print(res)
    print(res2)
    print(res3)