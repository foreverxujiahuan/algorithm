from typing import List


class Solution:

    def countPairs(self, coordinates, k):
        count = 0
        distance_count = dict()

        for x, y in coordinates:
            for px, py in distance_count:
                dx = x ^ px
                dy = y ^ py
                if dx + dy == k:
                    count += distance_count[(px, py)]  # 如果找到了符合距离的点，累加到count中
            distance_count[(x, y)] = distance_count.get((x, y), 0) + 1  # 更新当前点的距离记录

        return count



if __name__ == '__main__':
    solution = Solution()
    coordinates = [[27, 94], [61, 68], [47, 0], [100, 4], [127, 89], [61, 103], [26, 4], [51, 54], [91, 26], [98, 23], [80, 74],
     [19, 93]]
    k = 95
    res = solution.countPairs(coordinates, k)
    print(res)