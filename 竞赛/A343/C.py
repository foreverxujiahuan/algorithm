from typing import List


class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        specialRoads = [[x1, y1, x2, y2, cost] for (x1, y1, x2, y2, cost) in specialRoads
                        if abs(x1 - x2) + abs(y1 - y2) > cost]
        specialRoads.sort(key=lambda d: (d[0], d[1]))
        cur_x, cur_y = start[0], start[1]
        all_cost = 0
        target_x, target_y = target
        for road in specialRoads:
            [x1, y1, x2, y2, cost] = road
            raw_cost = abs(x1 - target_x) + abs(y1 - target_y)
            new_cost = abs(x2 - target_x) + abs(y2 - target_y)
            if raw_cost - new_cost < cost:
                continue
            cost1 = abs(x2 - cur_x) + abs(y2 - cur_y)
            cost2 = abs(x1 - cur_x) + abs(y1 - cur_y) + cost
            mi_cost = min(cost1, cost2)
            if abs(target_x - cur_x) + abs(target_y - cur_y) < mi_cost + abs(x2 - target_x) + abs(y2 - target_y):
                continue
            all_cost += mi_cost
            cur_x, cur_y = x2, y2
        all_cost += abs(cur_x - target_x) + abs(cur_y - target_y)
        return all_cost


if __name__ == '__main__':
    solution = Solution()
    # start = [1, 1]
    # target = [4, 5]
    # specialRoads = [[1, 2, 3, 3, 2], [3, 4, 4, 5, 1]]
    # start = [3, 2]
    # target = [5, 7]
    # specialRoads = [[3, 2, 3, 4, 4], [3, 3, 5, 5, 5], [3, 4, 5, 6, 6]]
    # start = [1, 1]
    # target = [5, 10]
    # specialRoads = [[3, 4, 5, 2, 5], [4, 5, 3, 8, 3], [3, 2, 5, 3, 1]]
    # start = [1, 1]
    # target = [9, 3]
    # specialRoads = [[6, 3, 9, 1, 1], [7, 1, 6, 3, 1], [7, 3, 4, 2, 2], [3, 3, 1, 1, 2]]
    start = [1, 1]
    target = [10, 9]
    specialRoads = [[5, 2, 3, 6, 3], [5, 6, 9, 5, 3], [5, 9, 1, 2, 5], [8, 6, 9, 8, 1]]
    res = solution.minimumCost(start, target, specialRoads)
    print(res)